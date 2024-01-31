## Alternative Azure DB for vector search
In order to use other azure db products such as cosmodb mongodb vcore, please follow the steps below:

(1) Install pf-azuredb library
- a) from source: [https://github.com/microsoft/pf-azuredb]
- b) from pypi: (coming soon)

(2) Make sure you add the database connection. For example, run the following command for cosmosdb mongodb connection. The python file is located in the connections folder.  
```
python connect_cosmos.py
```
Also, note that you need to whitelist your ip address to stablish connection to the database. 
(3) In you flow.dag.yaml click + symbol and select the intended tool. Please use example-flow to get an idea of how vector search can be done using the tool, then incorporate it your main flow.dag.yaml file, which is located in rag-copilot folder.

