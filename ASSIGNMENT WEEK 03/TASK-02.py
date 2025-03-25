'''
2. Create a program that reads a text file, searches for a specified word or
phrase, and replaces all occurrences with another word or phrase. Write
the modified content back to the file. Handle all possible exceptions as
well.

'''

def replace_in_file(file_path, search_word, replace_word):
    try:
       
        with open(file_path, 'r') as file:
            content = file.read()

        modified_content = content.replace(search_word, replace_word)

       
        with open(file_path, 'w') as file:
            file.write(modified_content)

        print("The file has been updated successfully.")
        with open(file_path, 'r') as file:
            content = file.read()
            print("The updated content is:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied to access the file '{file_path}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    search_word = input("Enter the word/phrase to search for: ")
    replace_word = input("Enter the word/phrase to replace with: ")

    replace_in_file(file_path, search_word, replace_word)
