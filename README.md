# Promptflow rag project template

The overall intention of this repo is to host the end-to-end process for building RAG applications, showcasing development, evaluation, experimentation, and deployment aspects using PromptFlow, Azure AI Studio, and other Azure data products.

The repo is currently hosting a single use-case on using PromptFlow and Azure AI for development, evaluation, and deployment of a RAG-based chatbot for question and answering on financial transcripts. In this sample, we also demonstrate how to use other Azure database offerings for vector searches. 

### Prerequisites
Before you begin, ensure that you have the following installed on your machine:

Python 3.9 or later,  VSCode, PromptFlow for VSCode extension, Docker

## Walkthrough: RAG on financial transcripts sample 


### Steps to run locally, experiment, deploy

#### 1. Run locally in your vscode:

   1) Set up your dev environment:
   Install miniconda for your environment, here is the link for [windows miniconda](https://docs.conda.io/projects/miniconda/en/latest/index.html). Run the following command
   `conda env update -f environment.yaml`
   2) Install [azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli) if you haven't already. Do `az-login`.
   3) Make a copy of `.env.sample` and rename it to `.env`. You can use this file to decide to use keys from this file or azure keyvault. The keys will be used for preprocessing in step 3 and creating connections for promptflow in step 4.
   ```bash
   # Use .env or keyvault. ENV or empty = .env, KEYVAULT = keyvault
   KEYS_FROM="ENV"
   KEY_VAULT_NAME=""
   ```
   > NOTE: Our convention is that variables from keyvault have a (-), but from a `.env` has a (_) like `OPENAI-API-BASE` vs. `OPENAI_API_BASE`
   4) cd to the `preprocessing/` folder and start running the preprocessing notebooks to create a new vector database index if you haven't done so already.
   5) Create connections for ACS, AOAI, etc by running python code in `connections/` directory.
   6) Go to `rag-copilot` directory, open flow.dag.yaml visually, then choose the connections that you have created in any specific nodes that are complaining with a warning.
   7) Run or build locally to deploy the app and interact with the bot in your local environment. 

    **Note**: You will find two yaml files in the 'rag-copilot' folder. The flow.dag.yaml is the main yaml file that orchestrates various app components, such as retreivals, llm calls, etc. In addition, you will find the hyperparameters of the flow inside the param_config.yaml. As an example, the changes you make to topK in param_config.yaml file will be reflected in the flow.dag.yaml at the run time. 

    **Known issue**: In addition to end-to-end running and debugging, promptflow allows single node runs for tests and debugging. However, please be aware that node running on its own that depend on configloader node will not work today. 

#### 2. Run experiments using the promptflow CLI

1. Definitions:
   1. Generation flow: the flow that generates `generated_answers`
   2. Evaluation flow: the flow that evaluates `generated_answers` and `retrieval` vs benchmark
2. Run your generation flow locally `pf run create --flow ./financial_transcripts/rag-copilot --data ./financial_transcripts/datasets/evalset.csv`
3. Run your evaluation flow locally `pf run create --flow ./financial_transcripts/evaluator/eval_multiple_score --run rag_copilot_variant_0_20240318_215835_391113
4. Run your evaluation flow remotely on Azure AI Studio `pfazure run create --flow ./evaluation./eval_multiple_score/ --run rag_copilot_variant_0_20240318_215835_391113 --resource-group appliedai --workspace-name appliedaistudioproject

#### 2. Steps for batch evaluation in vscode:

   1) Go to rag-copilot directory, open flow.dag.yaml
   2) Click batch run 
   3) When selecting input source, choose evalset.csv.
   4) Then choose the data mapping on the run yaml file. 
   You may either delete topK and maxTokens to use default values or provide integers for the desired values. Do not select them from data mapping as they will not be available
   5) The click run on the yaml file. 
   Once the run is completed, then you need to
   6) Go to evaluator directory and choose one of the folders and open the flow.dag.yaml file. Note that each folder presents one or many evaluation metrics.
   7) Click the batch run to start an evaluation flow. 
   8) when prompted, choose "existing run" since we are going to use the results of the main rag flow for the evaluation flow. 
   9) Choose the run in step 5 of the evaluation 
   10) This will create a run yaml file. You need to uncomment the data to be able to chose the evalset.csv again. You may need to use some columns such as ground truth answers. 
   11) Choose the column mapping for the necessary inputs.
   12) Note the name of the output file in your terminal.
   13) Click on the promptflow icon on the left ribbon of vscode
   14) Go to "Batch Run History" section and choose your recent run(s), then click on the Visualize.

#### 3. Experimentation in vscode

   1) Similar to step a.3 open the flow.dag.yaml file. Locate a prompt node and clone it. It will create a new variant and associated jinja file. Make the changes to the prompt in the jinja file. You may also make the changes to the openai variables such as temperature in the cloned node in the flow.dag.yaml. You may create multiple variants for cloneable nodes. Then save the file. 
   2) Finally, go through all the steps for the batch evaluations again to obtain evaluations for all the variants and compare the results. 

#### 4. Steps for batch experimentation using python SDK:

   1. Open batchRunEvaluations.ipynb notebook in the financial transcripts folder and run through cells. Note: to setup the configs for the batch experimentation runs, you may modify run_config.yaml file for the last section in the notebook. 

#### 5. Steps for docker deployment

1. pre-requisite: Docker. You can get docker from [here](https://www.docker.com/get-started/).
 2.  Change directory to sample folder (e.g. financial_transcripts)

 3) Use the command below to recreate your llm app as a docker format:

 ```bash
 pf flow build --source ./rag-copilot --output deploy --format docker
 ```
 >Note: the deploy folder is where the llm app is packaged. 
 
 3) Inspect the requirement.txt file in the 'deploy/flow' directory. If empty, please manually add all the python packages from the environment.yaml file located at the root directory.
 
 4) Inspect the connection files in the 'deploy/connections' and double-check information such as api_base and api_version.
 
 5) Build the docker image file by running the following command in the `financial_transcipts/` folder.
 ```docker build deploy -t rag-app-serve```
 
 6) Run with docker run. Make sure to add secret values in the command below:
 
 ```
 docker run -p 8080:8080 -e AOAI_CONNECTION_API_KEY=<secret-value> -e ACS_CONNECTION_API_KEY=<secret-value> rag-app-serve
 ```
 >Note: check the port mapping and change if needed. 
 
 7) Finally inspect the end point. 
 In you local machine, you may inspect your app in a browser: http://localhost:8080/

## Alternative Azure Vector databases
Microsft azure databases, such as cosmosdb mongodb vcore or postgres flex, also offer vector search capabilities that could be used in lieu of azure search. Please refer to vectordb-tools directory for the instructions.

## Developer guide

For any contributions, please make sure to check the Python formatting with Black formatter. 

## Contributing

Let's Expand this repo to interesting and more complex rag-applications. 

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
