
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def chat_flow(check_existing_context: bool, filter: {}, searchType: str) -> str:
    if check_existing_context == False and filter != {} and "filter" in searchType:
        return "new_retrieval"
    elif check_existing_context == False and filter != {} and "filter" not in searchType:
        return "new_retrieval"
    elif check_existing_context == False and filter == {} and "filter" in searchType:
        return "new_retrieval_need_filter"
    elif check_existing_context == False and filter == {} and "filter" not in searchType:
        return "new_retrieval"
    elif check_existing_context == True and filter != {} and "filter" in searchType:
        return "new_retrieval"
    elif check_existing_context == True and filter != {} and "filter" not in searchType:
        return "new_retrieval"
    elif check_existing_context == True and filter == {} and "filter" in searchType:
        return "use_same_context"
    elif check_existing_context == True and filter == {} and "filter" not in searchType:
        return "new_retrieval" # "use_same_context_and_new_retrieval"
    else:
        return "error"
