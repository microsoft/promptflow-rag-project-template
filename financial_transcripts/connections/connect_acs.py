from promptflow import PFClient
from promptflow.entities import AzureOpenAIConnection, CustomConnection, CognitiveSearchConnection
from dotenv import dotenv_values

config = dotenv_values('.env')
#print(config)
#Get a pf client to manage connections
pf = PFClient()

# Initialize an AzureOpenAIConnection object
connection = CognitiveSearchConnection(
    name = "acs_connection",
    api_key= config["AZURE_AI_SEARCH_KEY"],
    api_base=config["AZURE_AI_SEARCH_ENDPOINT"],
)

# # Create the connection, note that api_key will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)
