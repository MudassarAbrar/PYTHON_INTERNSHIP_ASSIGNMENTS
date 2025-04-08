'''
You have a text document that contains dates in various formats such as
12/09/2023, 2023-09-12, and Sep 12, 2023. Write a Python script that
uses regular expressions to extract all dates in these formats from the
text.
'''

import re

text ="""
The event is scheduled for 12/09/2023, but the meeting was rescheduled to 2023-09-12. 
The final report will be submitted on Sep 12, 2023.
"""

date_pattern = r'(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|[A-Za-z]{3} \d{2}, \d{4})'

dates = re.findall(date_pattern, text)


print("Extracted dates:", dates)
