'''
You have a text document that contains dates in various formats such as
12/09/2023, 2023-09-12, and Sep 12, 2023. Write a Python script that
uses regular expressions to extract all dates in these formats from the
text.
'''

import re

file_path = "dates.txt"

date_pattern = r'(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|[A-Za-z]{3} \d{2}, \d{4})'

# Open and read the file
with open(file_path, 'r') as file:
    text = file.read()

# Find all dates using the regular expression pattern
dates = re.findall(date_pattern, text)

# Output the list of dates found
print("Extracted dates:", dates)
