
from promptflow import tool
import re


@tool
def parse_score(score: str):
    return float(extract_float(score))


def extract_float(s):
    match = re.search(r"[-+]?\d*\.\d+|\d+", s)
    if match:
        return float(match.group())
    else:
        return None