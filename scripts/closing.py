"""Shared final brand line and deduplication for both output formats."""
from copy import deepcopy
import re
CLOSING = "Iga number räägib oma loo. Iga kivi kannab oma energiat."

def normalize_closing(data):
    """Remove existing closing sentences from text blocks; builders append one at the end."""
    result = deepcopy(data)
    patterns = [r"Iga\s+number\s+räägib\s+oma\s+loo\s*\.",
                r"Iga\s+kivi\s+kannab\s+oma\s+energiat\s*\."]
    pages = []
    for page in result['pages']:
        blocks = []
        for block in page:
            if 'text' in block:
                value = block['text']
                for pattern in patterns:
                    value = re.sub(pattern, '', value, flags=re.IGNORECASE)
                value = value.strip()
                if not value:
                    continue
                block['text'] = value
            blocks.append(block)
        if blocks:
            pages.append(blocks)
    result['pages'] = pages
    return result
