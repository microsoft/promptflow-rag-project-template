
from promptflow import tool
from typing import Tuple
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    AzureChatCompletion,
    AzureTextEmbedding,
)
import asyncio
import datetime

async def populate_memory(kernel: sk.Kernel, num_history: int, query: str, reply: str, context: str) -> None:
    await kernel.memory.save_information(
        collection="conversation_{}".format(num_history),
        id=datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z"),
        text=query,
    )
    await kernel.memory.save_information(
        collection="conversation_{}".format(num_history),
        id=datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z"),
        text=reply,
    )
    await kernel.memory.save_information(
        collection="conversation_{}".format(num_history),
        id=datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z"),
        text=context,
    )

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def call(query: str, reply: str, memory_dict: {}) -> str:
    kernel = memory_dict["kernel"]
    context = memory_dict["result"]
    num_history = 1
    asyncio.run(populate_memory(kernel, num_history, query, reply, context))
