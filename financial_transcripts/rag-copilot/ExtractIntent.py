from promptflow import tool
import re

@tool
def extract_intent(input: str, query: str):
    # Extract ticker using regular expression
    ticker_match = re.search(r'\bticker\s+(\w+)', query, re.IGNORECASE)
    ticker = ticker_match.group(1) if ticker_match else None

    # Extract year using regular expression
    year_match = re.search(r'\byear\s+(\d{2})', query, re.IGNORECASE)
    year = int(year_match.group(1)) if year_match else None

    # Extract quarter using regular expression
    quarter_match = re.search(r'\bquarter\s+(\d)', query, re.IGNORECASE)
    quarter = quarter_match.group(1) if quarter_match else None

    return {
      'Ticker': ticker,
      'Year': str(year),
      'Quarter': quarter
    }