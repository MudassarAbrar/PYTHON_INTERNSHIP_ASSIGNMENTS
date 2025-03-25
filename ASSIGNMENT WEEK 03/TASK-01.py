'''
1. Write a Python program that reads a text file, counts the number of
characters in it, and prints the total word count. Handle all possible
exceptions as well.

'''

try:
    with open("text_file.txt", "r") as file:
        data = file.read()
        print("Number of Characters in the file: ", len(data))
        print("Number of Words in the file: ", len(data.split()))
except FileNotFoundError:
    print("Error: The file 'text_file.txt' was not found.")
except IOError:
    print("Error: An I/O error occurred while handling the file.")
except Exception as e:
    print("An unexpected error occurred:", e)
