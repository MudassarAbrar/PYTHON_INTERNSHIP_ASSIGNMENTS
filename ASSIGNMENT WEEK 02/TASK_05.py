'''
Write a Python function to multiply all the numbers in a list.
'''

def multiply(l):
    multiply = 1
    for x in l:
        multiply*=x
    return multiply



user_list = map(int,input("ENTER A COMMA SEPERATED LIST: ").split(","))

print(multiply(user_list))