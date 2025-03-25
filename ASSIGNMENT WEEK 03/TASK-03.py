'''
3. Write a python program that takes any two lists from user having same
number of elements. Make a dictionary from these two lists in such a
way that first element of first list will be key and first element of second
list will be its associated value and so on. Store the dictionary in a text
file. Handle all possible exceptions as well. Note: do not use any library.
Make logic yourself.


'''
def create_dict_from_lists(list1, list2):
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i].strip()] = list2[i].strip() 
        
    return dictionary

def write_function(dictionary):
    try:
        with open("file.txt", "w") as file:
            file.write(str(dictionary))
            print("The dictionary has been written to the file successfully.")
            
        with open("file.txt", "r") as file:
            content = file.read()
            print("The content of the file is:")
            print(content)
    except IOError as e:
        print(f"File operation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during file handling: {e}")

def main():
    try:
        list1 = input("Enter the first list (comma-separated): ").split(",")
        list2 = input("Enter the second list (comma-separated): ").split(",")

        if len(list1) != len(list2):
            raise ValueError("The lists must have the same number of elements.")

        dictionary = create_dict_from_lists(list1, list2)
        write_function(dictionary)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
