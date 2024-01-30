
from promptflow import tool, ToolProvider
from promptflow.connections import AzureOpenAIConnection
from typing import Tuple
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    AzureChatCompletion,
    AzureTextEmbedding,
)
import asyncio
import datetime

class SKMemoryWithInit(ToolProvider):
    def __init__(self, modelConnection: AzureOpenAIConnection):
        super().__init__()
        self.modelConnection = modelConnection
        
        self.kernel = sk.Kernel()

        api_key = self.modelConnection["api_key"]
        endpoint = self.modelConnection["api_base"]
        azure_chat_service = AzureChatCompletion(deployment_name="gpt-35-turbo", endpoint=endpoint, api_key=api_key)
        azure_text_embedding = AzureTextEmbedding(deployment_name="text-embedding-ada-002", endpoint=endpoint, api_key=api_key)

        self.kernel.add_chat_service("chat_completion", azure_chat_service)
        self.kernel.add_text_embedding_generation_service("ada", azure_text_embedding)

        self.kernel.register_memory_store(memory_store=sk.memory.VolatileMemoryStore())
        #self.kernel.import_plugin(sk.core_plugins.TextMemoryPlugin())

    # The inputs section will change based on the arguments of the tool function, after you save the code
    # Adding type to arguments and return value will help the system show the types properly
    # Please update the function name/signature per need
    @tool
    def call(self, query: str, context: str) -> str:
        result = asyncio.run(self.kernel.memory.search("conversation_{}".format(1), query))
        if len(result) == 0:
            return {
                "result": [],
                "kernel": self.kernel,
            }
        else:
            return {
                "result": result[0].text,
                "kernel": self.kernel,
            }

