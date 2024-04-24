import requests  
import json  
import pdb
import os
import pandas as pd
from event_stream import EventStream
import time
import argparse

parser = argparse.ArgumentParser(description='Get a URL endpoint')  
parser.add_argument('--url', type=str, help='URL endpoint to be parsed', default="http://localhost:8080/score")  
  
args = parser.parse_args() 

url = args.url

def apply_delta(base: dict, delta: dict):
    for k, v in delta.items():
        if v == None:
            pass
        else:
            if k in base:
                base[k] += v
            else:
                base[k] = v

print("Starting chat experience, hit CTRL+C to exit")
print()

store_current_history = []
headers = {"Content-Type": "application/json", "Accept" : "text/event-stream, application/json"}  
initial_run = True
start_stream = True
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
    response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)  
    event_stream = EventStream(response.iter_lines())
    response_dict = {}
    for i, event in enumerate(event_stream):
        if i == 0:
            first_token = time.time()
        dct = json.loads(event.data)
        apply_delta(response_dict, dct)
        if "reply" in response_dict.keys():
            if start_stream == True:
                print("AI reply: {}".format(dct['reply']), end='', flush=True) 
                start_stream = False
            else:
                print("{}".format(dct['reply']), end='', flush=True) 
    end_time = time.time()
    print()
    print()

    response_dict["chat_history"] = [{"inputs": {"query": question}, "outputs": {"reply": response_dict["reply"]}}]
    df = pd.DataFrame({'question': [question], 'reply': [response_dict['reply']], 'chat_history': [store_current_history], 'first_token_time': [first_token - start_time], 'call_time': [end_time - start_time]})

    if initial_run:
        df.to_csv('stream_result.csv', index=False, mode='w')
        initial_run = False
    else:
        df.to_csv('stream_result.csv', index=False, mode='a', header=False)
    
    start_stream = True
print('Complete')