
from promptflow import tool
import yaml

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(config_yaml: str) -> str:
    with open('./'+ config_yaml, "r") as file:
        rag_config = yaml.safe_load(file)
    return rag_config
