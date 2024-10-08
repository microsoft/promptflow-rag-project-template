import json
from promptflow import tool


@tool
def format_retrieved_documents(docs: list, maxTokens: int) -> str:
    formattedDocs = []
    strResult = ""
    for index, document in enumerate(docs):
        formattedDocs.append({f"[doc[{index}]": {"content": document}})
        formattedResult = {"retrieved_documents": formattedDocs}
        nextStrResult = json.dumps(formattedResult)
        if estimate_tokens(nextStrResult) > maxTokens:
            break
        strResult = nextStrResult

    if strResult == "":
        return json.dumps({"retrieved_documents": []})
    return strResult


def estimate_tokens(text: str) -> int:
    return (len(text) + 2) / 3


# import json
# from promptflow import tool

# @tool
# def format_retrieved_documents(docs: list, maxTokens: int) -> str:
#   formattedDocs = []
#   strResult = ""
#   for index, doc in enumerate(docs):
#     formattedDocs.append({
#       f"[doc{index}]": {
#         "ticker": doc['symbol'],
#         "quarter": doc['fiscalquarter'],
#         "year": doc['fiscalyear'],
#         "content": doc['content']
#       }
#     })
#     formattedResult = { "retrieved_documents": formattedDocs }
#     nextStrResult = json.dumps(formattedResult)
#     if (estimate_tokens(nextStrResult) > maxTokens):
#       break
#     strResult = nextStrResult

#   if strResult == "":
#     return json.dumps({"retrieved_documents": []})
#   return strResult

# def estimate_tokens(text: str) -> int:
#   return (len(text) + 2) / 3
