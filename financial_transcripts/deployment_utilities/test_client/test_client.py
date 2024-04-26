import requests  
import json  
import pdb
import os
import pandas as pd
import time
import argparse

parser = argparse.ArgumentParser(description='Get a URL endpoint')  
parser.add_argument('--url', type=str, help='URL endpoint to be parsed', default="http://localhost:8080/score")  
  
args = parser.parse_args() 

url = args.url

print("Starting chat experience, hit CTRL+C to exit")
print()

store_current_history = []
headers = {"Content-Type": "application/json"}  
initial_run = True
while True:
    question = input("user question: ")
    if initial_run == True:
        data = {
            "query": question,
            "chat_history": [],
        }  
    else:
        data = {
            "query": question,
            "chat_history": response_dict["chat_history"],
        }  
        store_current_history = response_dict["chat_history"].copy()

    start_time = time.time()
    response = requests.post(url, data=json.dumps(data), headers=headers)  
    response_dict = json.loads(str(response.text))
    end_time = time.time()

    print("AI Reply: ", response_dict['reply'])
    print() 

    response_dict["chat_history"] = [{"inputs": {"query": question}, "outputs": {"reply": response_dict["reply"]}}]
    df = pd.DataFrame({'question': [question], 'reply': [response_dict['reply']], 'chat_history': [store_current_history], 'call_time': [end_time - start_time]})

    if initial_run:
        df.to_csv('result.csv', index=False, mode='w')
        initial_run = False
    else:
        df.to_csv('result.csv', index=False, mode='a', header=False)
print('Complete')