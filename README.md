# copilot rag samples 

This repo is a collection of samples on using promptflow and azure ai for development and evaluation of rag applications. 
To run each sample go the specific folder. In this case, let me walk you through the financial_transcript sample. Please go to the folder and follow the instructions for running a rag app locally and performing evaluations. 
steps to run rag app locally:
1) Follow prompt flow documentation to set up your promptflow python env:
https://microsoft.github.io/promptflow/how-to-guides/quick-start.html
2) Create connections for ACS, AOAI, etc by running python code in connections directory. 
3) Go to rag-copilot directory, open flow.dag.yaml, then choose the connections that you have created. Build locally to deploy the app and interact with the bot in your local environment. 
Note: the assumption is that the search index has previously been created. 

Steps for batch evaluation:
1) Go to rag-copilot directory, open flow.dag.yaml
2) Click batch run 
3) When selecting input source, choose evalset.csv.
4) Then choose the data mapping on the run yaml file. 
5) The click run on the yaml file. 
Once the run is completed, then you need to
6) Go to evaluator directory and choose one of the folders and open the flow.dag.yaml file. Note that each folder presents one or many evaluation metrics.   
7) Click the batch run to start an evaluation flow. 
8) when prompted, chose "existing run" since we are going to use the results of the main rag flow for the evaluation flow. 
9) Choose the run in step 1 of the evaluation 
10) This will create a run yaml file. You need to uncomment the data to be able to chose the evalset.csv again. You may need to use some columns such as ground truth answers. 
11) Choose the column mapping for the necessary inputs.
12) Note the name of the output file in your terminal.
13) Click on the promptflow icon on the left ribbon of vscode
14) Go to "Batch Run History" section and choose your recent run(s), then click on the Visualize.

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
