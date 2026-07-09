import re

def clean_markdown(md: str) -> str:
    md = re.sub(r"\(cid:\d+\)", "", md)
    md = md.replace("§", "")
    md = md.replace("ï", "")
    return md