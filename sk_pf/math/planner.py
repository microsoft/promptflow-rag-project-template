import asyncio
from promptflow import tool

import semantic_kernel as sk
from semantic_kernel.planning.sequential_planner import SequentialPlanner
from plugins.Math import Math as Math
from promptflow.connections import (
    AzureOpenAIConnection,
)

from semantic_kernel.connectors.ai.open_ai import (
    AzureChatCompletion,
    AzureTextCompletion,
)

@tool
def my_python_tool(
    input: str,
    deployment_name: str,
    modelConnection: AzureOpenAIConnection,
) -> str:
    # Initialize the kernel
    kernel = sk.Kernel()

    kernel.add_chat_service(
        "chat_completion",
        AzureChatCompletion(
            deployment_name,
            endpoint=modelConnection.api_base,
            api_key=modelConnection.api_key,
        ),
    )

    planner = SequentialPlanner(kernel=kernel)

    # Import the native functions
    math_plugin = kernel.import_skill(Math(), "MathPlugin")

    ask = "Use the available math functions to solve this word problem: " + input

    plan = asyncio.run(planner.create_plan_async(goal=ask))

    # Execute the plan
    result = asyncio.run(plan.invoke_async())

    for index, step in enumerate(plan._steps):
        print("Function: " + step.skill_name + "." + step._function.name)
        print("Input vars: " + str(step.parameters.variables))
        print("Output vars: " + str(step._outputs))
    print("Result: " + str(result))

    return str(result)