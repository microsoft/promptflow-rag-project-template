from promptflow import tool
import re

@tool
def query_parser(query: str):
    # Extract year
    year = re.search(r'FY(\d{2})', query).group(1)

    # Extract quarter
    quarter = re.search(r'Q(\d)', query).group(1)

    return {
      'Year': str(year),
      'Quarter': quarter
    }