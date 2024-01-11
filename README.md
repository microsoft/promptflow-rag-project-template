# Promptflow rag samples 

This repo is a collection of samples on using promptflow and azure ai for development and evaluation of rag applications. 
To run each sample go the specific folder. 

### Prerequisites
Before you begin, ensure that you have the following installed on your machine:

Python 3.9 or later,  VSCode, PromptFlow for VSCode extension

## Example walkthrough: RAG on financial transcripts sample 


### Steps

a. steps to run rag app locally in your vscode:

1) Set up your dev environment:
Follow prompt flow documentation to set up your promptflow python env:
https://microsoft.github.io/promptflow/how-to-guides/quick-start.html
Preferably, use the environment.yaml file at the root directory to install all the dependancies needed to run the samples.

2) Create connections for ACS, AOAI, etc by running python code in connections directory. For this step you will need to have all your keys in a '.env' file in the connections folder. 
3) Go to rag-copilot directory, open flow.dag.yaml, then choose the connections that you have created. Build locally to deploy the app and interact with the bot in your local environment. 
Note: the assumption is that the search index has previously been created. if not, you may go through the notebooks in the preprocessing folder to create a search index. 

b. Steps for batch evaluation in vscode:

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

c. Steps for experimentation in vscode:

1) Similar to step a.3 open the flow.dag.yaml file. Locate a prompt node and clone it. It will create a new variant and associated jinja file. Make the changes to the prompt in the jinja file. You may also make the changes to the openai variables such as temperature in the cloned node in the flow.dag.yaml. You may create multiple variants for cloneable nodes. Then save the file. 
2) Finally, go through all the steps for the batch evaluations again to obtain evaluations for all the variants and compare the results. 

d. Steps for batch experimentation using python SDK:
1) Open batchRunEvaluations.ipynb notebook in the financial transcripts folder and run through cells. Note: to setup the configs for the batch experimentation runs, you may modify run_config.yaml file for the last section in the notebook. 

## Contributing

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
