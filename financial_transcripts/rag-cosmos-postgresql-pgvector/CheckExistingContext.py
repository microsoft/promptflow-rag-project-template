
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def check_existing_context(history: list) -> str:
    if len(history) == 0:
        return False
    else:
        try:
            retrieved_docs = history[-1]["outputs"]["fetched_docs"]
            already_retrieved = True
        except:
            already_retrieved = False
    return already_retrieved
