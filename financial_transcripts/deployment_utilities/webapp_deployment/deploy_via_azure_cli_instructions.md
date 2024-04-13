**To deploy to Azure web app from the Docker container**
   1. *Optional* if already setup: Create the ACR and web-app services. Note: any of the `<ACR-name>, <RG-name>, etc. are arbitrarily defined`
      1. Ensure you are creating [your services on the correct subscription](https://learn.microsoft.com/en-us/cli/azure/manage-azure-subscriptions-azure-cli)
         1. `az account list --output table` to list all subscriptions available to you
         2. `az account show --output table` to show which subscription is currently set to
         3. `az account set --subscription "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` to set a subsrciption using a subscription-id
      2. Create a container registry ` az acr create --name <ACR-NAME> --resource-group <RG-NAME> --sku basic --admin-enabled true`
      3. Create a web app service plan `az appservice plan create --resource-group <RG-NAME> --name <APP-SERVICE-PLAN-NAME> --location eastus --is-linux --sku B2` (please make sure to to use B2 for promptflow deployments)
   2. Build the docker container remotely (this will upload and build the container in your ACR service) `az acr build --registry <ACR-NAME> --resource-group <RG-NAME> --image <rag-app-image-name> .`
   3. Create a web app using the built container `az webapp create --resource-group <RG-NAME> --plan <APP-SERVICE-PLAN-NAME> --name <RAG-WEBAPP-NAME> -i <ACR-NAME>.azurecr.io/<rag-app-image-name>:latest`
   plase double check the deployment center section of the web app on the azure portal to ensure image is pulled correctly.  
   4. Configure your web app to listen to port 8080 and set a longer container_start_time_limit `az webapp config appsettings set --resource-group <RG-NAME> --name <RAG-WEBAPP-NAME> --settings WEBSITES_PORT=8080 WEBSITES_CONTAINER_START_TIME_LIMIT=1800 `
   5. Configure your web app for environment variables, such as open_ai_key. Please make sure to use 
    `az webapp config appsettings set --resource-group <RG-NAME> --name <RAG-WEBAPP-NAME> --settings APENAI_CONNECTION_API_KEY=<open_ai_key>`
   6. Open a browser at `<RAG-WEBAPP-NAME>.azurewebsites.net` (note: it may take a few minutes to load the first time the container is started)