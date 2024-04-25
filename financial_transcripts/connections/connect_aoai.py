from promptflow.client import PFClient
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
    connection = AzureOpenAIConnection(
        name="aoai_connection",
        api_key=client.get_secret("OPENAI-API-KEY").value,
        api_base=client.get_secret("OPENAI-API-BASE").value,
        api_version=client.get_secret("OPENAI-API-VERSION").value,
    )
else:
    print(".env was selected.")
    # Initialize an AzureOpenAIConnection object
    connection = AzureOpenAIConnection(
        name="aoai_connection",
        api_key=config["OPENAI_API_KEY"],
        api_base=config["OPENAI_API_BASE"],
        api_version=config["OPENAI_API_VERSION"],
    )

# # Create the connection, note that api_key will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)
