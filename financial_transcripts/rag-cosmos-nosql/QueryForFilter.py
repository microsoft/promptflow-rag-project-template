
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input_dict: str) -> str:
    return f"c.fiscal_year IN ('{input_dict['Year']}') and c.fiscal_quarter IN ('{input_dict['Quarter']}')"