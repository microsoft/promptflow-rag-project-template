
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def generate_result(chat_flow: str, determine_reply="", continue_reply="") -> str:
    if chat_flow == "new_retrieval_need_filter":
        return "Hi there! I am fully equipped to help you today, however, you have configured me to use a searchType that requires a filter. Please provide a filter and try again, which should look something like 'FY23Q1' or 'FY23 Q2'. Otherwise, you can change the searchType to one that does not require a filter. The choices are ['filter_vector', 'vector', 'hybrid', 'filter_hybrid', 'filter']."
    elif chat_flow != "error":
        if determine_reply:
            return determine_reply
        else:
            return continue_reply
    else:
        return "Error: My creators have not programmed me to handle this situation. Please contact them for assistance."