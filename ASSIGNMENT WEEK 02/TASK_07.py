'''

Write a python program that takes any two lists from user having same number of
elements. Make a dictionary from these two lists in such a way that first element of first
list will be key and first element of second list will be its associated value and so on and
print the result.
Do not use any library. Make logic yourself.

'''
try:
    list01 = input("ENTER THE FIRST LIST(comma-separated): ").split(",")

    list02 = input("ENTER THE SECOND LIST(comma-separated): ").split(",")
    
    if len(list01)!=len(list02):
        raise ValueError("LISTS AREN'T OF SAME LENGTH") 
    
    
    print("List are of same length")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
    
my_dict = {}
for i in range(len(list01)):
    my_dict[list01[i]] = list02[i]
    
        
print(my_dict)
        

