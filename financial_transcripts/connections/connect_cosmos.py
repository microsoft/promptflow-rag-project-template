from promptflow import PFClient
from promptflow.entities import CustomConnection
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import dotenv_values

config = dotenv_values('../../.env')

#Get a pf client to manage connections
pf = PFClient()

if config['KEYS_FROM'] == "KEYVAULT":
    print('keyvault was selected.')
    keyVaultName = config["KEY_VAULT_NAME"]
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    # Initialize a custom connection object
    connection = CustomConnection(
        name="cosmodb_connection", 
        # Secrets is a required field for custom connection
        secrets={"my_key": client.get_secret("COSMOS-DB-KEY").value},
        configs={
            "endpoint": client.get_secret("COSMOS_DB_API_ENDPOINT").value,
            "AZURE_COSMOSDB_MONGODB_URI": client.get_secret("COSMOS_DB_MONGODB_URI").value,}
    )
else:
    print('.env was selected.')
    # Initialize an AzureOpenAIConnection object
    connection = CustomConnection(
        name="cosmodb_connection", 
        # Secrets is a required field for custom connection
        secrets={"my_key": config["COSMOS_DB_API_KEY"]},
        configs={
            "endpoint": config["COSMOS_DB_API_ENDPOINT"],
            "AZURE_COSMOSDB_MONGODB_URI": config["COSMOS_DB_URI"],
        }
    )

# Create the connection, note that all secret values will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)