from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(filter: object, topK: int, maxTokens: int) -> object:
    config = {}
    config['filter'] = filter
    config['topK'] = topK
    config['maxTokens'] = maxTokens
    return config
