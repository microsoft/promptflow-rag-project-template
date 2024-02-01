import math
from semantic_kernel.plugin_definition import (
    kernel_function,
    kernel_function_context_parameter,
)
from semantic_kernel.orchestration.kernel_context import KernelContext


class Math:
    @kernel_function(
        description="Takes the square root of a number",
        name="Sqrt",
        input_description="The value to take the square root of",
    )
    def square_root(self, number: str) -> str:
        return str(math.sqrt(float(number)))

    @kernel_function(
        description="Adds two numbers together",
        name="Add",
    )
    @kernel_function_context_parameter(
        name="input",
        description="The first number to add",
    )
    @kernel_function_context_parameter(
        name="number2",
        description="The second number to add",
    )
    def add(self, context: KernelContext) -> str:
        return str(float(context["input"]) + float(context["number2"]))

    @kernel_function(
        description="Subtract two numbers",
        name="Subtract",
    )
    @kernel_function_context_parameter(
        name="input",
        description="The first number to subtract from",
    )
    @kernel_function_context_parameter(
        name="number2",
        description="The second number to subtract away",
    )
    def subtract(self, context: KernelContext) -> str:
        return str(float(context["input"]) - float(context["number2"]))

    @kernel_function(
        description="Multiply two numbers. When increasing by a percentage, don't forget to add 1 to the percentage.",
        name="Multiply",
    )
    @kernel_function_context_parameter(
        name="input",
        description="The first number to multiply",
    )
    @kernel_function_context_parameter(
        name="number2",
        description="The second number to multiply",
    )
    def multiply(self, context: KernelContext) -> str:
        return str(float(context["input"]) * float(context["number2"]))

    @kernel_function(
        description="Divide two numbers",
        name="Divide",
    )
    @kernel_function_context_parameter(
        name="input",
        description="The first number to divide from",
    )
    @kernel_function_context_parameter(
        name="number2",
        description="The second number to divide by",
    )
    def divide(self, context: KernelContext) -> str:
        return str(float(context["input"]) / float(context["number2"]))