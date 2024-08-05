from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
from promptflow.connections import CognitiveSearchConnection
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
import requests
from azure.core.credentials import AzureKeyCredential
import pdb

def get_query_embedding(query, endpoint, api_key, api_version, embedding_model_deployment):
    request_url = f"{endpoint}/openai/deployments/{embedding_model_deployment}/embeddings?api-version={api_version}"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    request_payload = {
        'input': query
    }
    embedding_response = requests.post(request_url, json = request_payload, headers = headers, timeout=None)
    if embedding_response.status_code == 200:
        data_values = embedding_response.json()["data"]
        embeddings_vectors = [data_value["embedding"] for data_value in data_values]
        return embeddings_vectors
    else:
        raise Exception(f"failed to get embedding: {embedding_response.json()}")

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def acs_retriever(queries: str, searchConnection: CognitiveSearchConnection, indexName: str, topK: int, embeddingModelConnection: AzureOpenAIConnection, embeddingModelName: str, vectorColName: str, searchType: str, filterCol):
    #  searchType options: "filter", "vector", "hybrid", filter_vector", "filter_hybrid"

    embeddingModelName = embeddingModelName if embeddingModelName != None else None

    search_client = SearchClient(
        endpoint=searchConnection["api_base"],
        index_name=indexName,
        credential=AzureKeyCredential(searchConnection["api_key"]),
    )

    searchType = searchType.lower()
    
    if searchType == "filter_vector" or searchType == "filter_hybrid" or searchType == "filter":
        filter_str = " and ".join(f"({key} eq '{value}')" for key, value in filterCol.items())
        filter_str = f"({filter_str})"
    else:
        filter_str = None

    if searchType == "vector" or searchType == "hybrid" or searchType == "filter_vector" or searchType == "filter_hybrid":
        queryEmbedding = get_query_embedding(
            query=queries,
            endpoint=embeddingModelConnection["api_base"],
            api_key=embeddingModelConnection["api_key"],
            api_version=embeddingModelConnection["api_version"],
            embedding_model_deployment=embeddingModelName
        )[0]

        vector_query = VectorizedQuery(vector=queryEmbedding, k_nearest_neighbors=topK, fields=vectorColName)
    else:
        vector_query=None

    if searchType == "filter":
        results = search_client.search(
            search_text=None,
            vector_queries=None,
            filter=filter_str,
            top=topK,
        )
    elif searchType == "vector" or searchType == None:
        results = search_client.search(
            search_text=None,
            vector_queries=[vector_query],
            filter=None,
            top=topK,
        )
    elif searchType == "hybrid":
        results = search_client.search(
            search_text=queries,
            vector_queries=[vector_query],
            filter=None,
            top=topK,
        )
    elif searchType == "filter_vector":
        results = search_client.search(
            search_text=None,
            vector_queries=[vector_query],
            filter=filter_str,
            top=topK,
        )
    elif searchType == "filter_hybrid":
        results = search_client.search(
            search_text=queries,
            vector_queries=[vector_query],
            filter=filter_str,
            top=topK,
        )
    else:
        raise ValueError('Please choose valid searchType from: ["filter", "vector", "hybrid", "filter_vector", "filter_hybrid"]')
    output = [result for result in results]

    return output
