# Test client to work with backend promptflow serving

Promptflow serving is deploying the backend flow for inference with an endpoint for consumption, but the provided gunicorn UI is not always desired. Customers can create their own front end UI and reach the promptflow served endpoint. [Promptflow serving](https://microsoft.github.io/promptflow/how-to-guides/deploy-a-flow/deploy-using-docker.html) via vscode deploys to a Docker image so that it can be run as a container, with REST API. This README discusses some important details when deploying because things like chat history are not handled the same way in deployment as experimentation. The experience in experimentation suggests that chat history is automatically accumulated and stored during deployment, but in fact the responsibility of handling chat history is placed on the client because the backend flow is stateless. This means the developers must consume the chat history as output from the backend and find a way to provide again as input to the backend flow. 

# Using the test client

The endpoint argument is optional and will default to `http://localhost:8080/score`. If you deploy to a static webapp, it will look like below

```cmd
python test_client.py --url <https://INSERT_NAME.azurewebsites.net/score>
```

## Streaming

[promptflow streaming](https://microsoft.github.io/promptflow/how-to-guides/enable-streaming-mode.html) can work with either an LLM node or a custom Python node with openAI sdk implementation. You need to specify `stream: true` in inputs of the LLM node you expect to stream, but this has to be done in `flow.dag.yaml`. For whatever reason, you cannot do it via the UI. If you are using a custom Python node with openAI sdk, then you need to specify `stream=True` in the Python API of the custom node and also use the generator (yield) instead of return. Whichever route you take for streaming, then you need to deploy via Docker. 

```
- name: ContinueReply
  type: llm
  source:
    type: code
    path: ContinueReply.jinja2
  inputs:
    deployment_name: gpt-35-turbo
    conversation: ${FormatConversation.output}
    context: ${GetContextFromHistory.output}
    user_query: ${inputs.query}
    stream: true
```

> NOTE: Streaming only works from the final LLM response in your flow. If you have more than one route and bypass certain nodes, be sure to enable stream: true for all of the potential final LLM responses. If you don't, you will likely get an error from the client saying that there was no response. On the promptflow serving side, you will see it say streaming was not enabled.

Streaming will then work if you modify the header in the client to include `text/event-stream`. 
```
"Accept" : "text/event-stream, application/json"
```

```cmd
python test_client_stream.py --url <https://INSERT_NAME.azurewebsites.net/score>
```