
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def generate_result(determine_reply="", continue_reply="") -> str:
    if determine_reply:
        return determine_reply
    else:
        return continue_reply
    return
