
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def generate_result(determine_reply="", continue_reply="", retrieved_docs={}, context={}) -> str:
    result = {}
    if determine_reply:
        result["retrieved_docs"] = retrieved_docs
        result["determine_reply"] = determine_reply
        return result
    else:
        result["retrieved_docs"] = context
        result["determine_reply"] = continue_reply
        return result