from promptflow import tool
import re
import pdb

@tool
def query_parser(query: str, conversation):
    try:
        # Extract year
        year = re.search(r'FY(\d{2})', query).group(1)

        # Extract quarter
        quarter = re.search(r'Q(\d)', query).group(1)

        return {
            'Year': str(year),
            'Quarter': quarter
        }
    except:
        last_query = conversation[0]['inputs']['query']
        # Extract year
        year = re.search(r'FY(\d{2})', last_query).group(1)

        # Extract quarter
        quarter = re.search(r'Q(\d)', last_query).group(1)

        return {
            'Year': str(year),
            'Quarter': quarter
        }