from promptflow import PFClient
from promptflow.entities import CustomConnection
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

#Get a pf client to manage connections
pf = PFClient()

# Initialize a custom connection object
connection = CustomConnection(
    name="cosmodb_connection", 
    # Secrets is a required field for custom connection
    secrets={"my_key": client.get_secret("COSMOS-DB-KEY").value},
    configs={
        "endpoint": config["COSMOS_DB_API_ENDPOINT"],
        "AZURE_COSMOSDB_MONGODB_URI": config["COSMOS_DB_MONGODB_URI"],}
)

# Create the connection, note that all secret values will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)