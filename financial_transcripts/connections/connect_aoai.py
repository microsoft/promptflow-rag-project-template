from promptflow import PFClient
from promptflow.entities import AzureOpenAIConnection, CustomConnection, CognitiveSearchConnection
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

#Get a pf client to manage connections
pf = PFClient()

# Initialize an AzureOpenAIConnection object
connection = AzureOpenAIConnection(
    name="aoai_connection", 
    api_key=client.get_secret("OPENAI-API-KEY").value,
    api_base=client.get_secret("OPENAI-API-BASE").value,
    api_version=client.get_secret("OPENAI-API-VERSION").value,
)

# # Create the connection, note that api_key will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)
