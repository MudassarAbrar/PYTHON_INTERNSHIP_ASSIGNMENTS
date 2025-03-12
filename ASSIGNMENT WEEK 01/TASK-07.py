'''

Write a Python program to get the largest number from a list input from user. use the
list given in task 3.
'''

#function using input from the user 



def largest_num(user_list):
    return max(user_list)



user_input = map(int,input("ENTER THE COMMA SEPERATED LIST:  ").strip().split(","))

print("user output")
print(largest_num(user_input))


#function using task 3 list


print("output of list(given)")

print(largest_num([2,4,6,5,3,8,2,6,6,4]))


