import re

def extract_numbers_from_markdown_table(md_text):
    """
    Extracts the first number in each row of a markdown table
    Assumes table format: | Month | Revenue |
    """
    lines = md_text.strip().split('\n')
    values = []
    for line in lines:
        if re.match(r'^\|\s*\w+', line):  # skip header/sep rows
            parts = line.strip().split('|')
            if len(parts) >= 3 and parts[2].strip().replace(',', '').isdigit():
                val = float(parts[2].strip().replace(',', ''))
                values.append(val)
    return values
