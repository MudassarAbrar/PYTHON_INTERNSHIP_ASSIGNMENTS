'''
Write a python program that take 10 inputs from the user using loop and append the
every user input value in the list and calculate the sum of all numbers.

'''

sum = 0

my_list = []

for x in range(10):
    user_data = int(input(f"ENTER THE '{x}' input : "))
    my_list.append(user_data)
    
    sum += my_list[x]
    
    
print(my_list)
print(sum)