'''
Write a program that should delete all elements in the list less than 4. use the list given
in task 3.

'''
numbers = [2, 4, 6, 5, 3, 8, 2, 6, 6, 4]


new_list = [x for x in numbers if x>=4]



print(new_list)