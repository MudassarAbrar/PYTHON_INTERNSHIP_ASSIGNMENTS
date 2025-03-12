'''
Write a Python function to check if the last letter of user input string is a vowel or a
consonant.

'''
def check(s):
    return "(TRUE) EXISTS" if s[-1] in [ 'a', 'e', 'i', 'o', 'u'] else "(FALSE) DOESN'T EXIST"


user_string = input("ENTER THE STRING TO CHECK: ")

print(check(user_string))
