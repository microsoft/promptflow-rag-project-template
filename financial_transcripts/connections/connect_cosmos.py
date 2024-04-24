from promptflow import PFClient
from promptflow.entities import CustomConnection
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import dotenv_values

config = dotenv_values("../../.env")

# Get a pf client to manage connections
pf = PFClient()

if config["KEYS_FROM"] == "KEYVAULT":
    print("keyvault was selected.")
    keyVaultName = config["KEY_VAULT_NAME"]
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    # Initialize a custom connection object
    connection = CustomConnection(
        name="cosmodb_connection",
        # Secrets is a required field for custom connection
        secrets={"AZURE_COSMOSDB_MONGODB_URI": client.get_secret(
                "COSMOS-DB-MONGO-URI"
            ).value})
    
else:
    print(".env was selected.")
    # Initialize an AzureOpenAIConnection object
    connection = CustomConnection(
        name="cosmodb_connection",
        # Secrets is a required field for custom connection
        secrets={ "AZURE_COSMOSDB_MONGODB_URI": config["COSMOS_DB_MONGO_URI"]},  # unsupported
    )

# Create the connection, note that all secret values will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)
