'''
4. Write a function that will take a number 'n' input by user and will return its factorial.

'''

def factorial(n):
    if n == 0:
        return 1 
    else: 
        return n*factorial(n-1) 
    
num = int(input("ENTER THE NUMBER: "))   
print(factorial(num))