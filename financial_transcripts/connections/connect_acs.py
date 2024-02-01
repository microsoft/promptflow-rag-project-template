from promptflow import PFClient
from promptflow.entities import (
    AzureOpenAIConnection,
    CustomConnection,
    CognitiveSearchConnection,
)
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

    # Initialize an AzureOpenAIConnection object
    connection = CognitiveSearchConnection(
        name="acs_connection",
        api_key=client.get_secret("COGSEARCH-API-KEY").value,
        api_base=client.get_secret("COGSEARCH-ADDRESS").value,
    )
else:
    print(".env was selected.")
    # Initialize an AzureOpenAIConnection object
    connection = CognitiveSearchConnection(
        name="acs_connection",
        api_key=config["COGSEARCH_API_KEY"],
        api_base=config["COGSEARCH_ADDRESS"],
    )

# # Create the connection, note that api_key will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)
