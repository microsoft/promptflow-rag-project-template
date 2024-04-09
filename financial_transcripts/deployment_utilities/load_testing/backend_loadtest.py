from locust import HttpUser, task, constant
import random
import json
from dotenv import dotenv_values

DEPLOYED_ENDPOINT = 'http://localhost:8080/' # or your azure deployment 'https://yourdeployent.azurewebsites.net/'

class QuickstartUser(HttpUser):
    wait_time = constant(0)
    host = DEPLOYED_ENDPOINT 
    
    @task
    def test_vectorindex_route(self):

        response = self.client.post("/score", data = json.dumps({
			"query": " What is the growth rate of Azure ML revenue in FY23Q1??",
            "chat_history": [],  # Session will start with an empty chat history
        }))

        
    def on_start(self):
        self.client.headers = {"Content-Type": "application/json"}