from promptflow import PFClient
from promptflow.entities import CustomConnection
from dotenv import dotenv_values

config = dotenv_values('.env')
#print(config)
#Get a pf client to manage connections
pf = PFClient()

# Initialize a custom connection object
connection = CustomConnection(
    name="cosmodb_connection", 
    # Secrets is a required field for custom connection
    secrets={"my_key": config["COSMOS_DB_API_KEY"]},
    configs={
        "endpoint": config["COSMOS_DB_API_ENDPOINT"],
        "AZURE_COSMOSDB_MONGODB_URI": config["COSMOS_DB_URI"]}
)

# Create the connection, note that all secret values will be scrubbed in the returned result
result = pf.connections.create_or_update(connection)
print(result)