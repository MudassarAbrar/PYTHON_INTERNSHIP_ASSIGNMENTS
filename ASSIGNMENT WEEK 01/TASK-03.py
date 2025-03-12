'''
Write a program to count all the even numbers in that given list and print the count.
list = [2,4,6,5,3,8,2,6,6,4]

'''


def even_no_count(given_list):
    
    return [x for x in given_list if x%2==0]

list = [2,4,6,5,3,8,2,6,6,4]

print(f'Even number in lists are "{even_no_count(list)}"')
print(f'Count of even numbers is "{len(even_no_count(list))}"')

