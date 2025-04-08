'''
7. You have a block of text that contains several email addresses scattered
throughout. Write a Python script that uses regular expressions to
extract all valid email addresses from the text.

'''

import re


text = """
Hello John, please contact me at john.doe@example.com for the project update.
Also, you can reach out to support@company.org for any issues. 
You can email my colleague at sarah123@workplace.co.uk for further assistance.
Additionally, mark.smith@domain.com is available for technical support.
"""

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, text)

print("Extracted email addresses:", emails)
