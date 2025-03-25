'''7. You need to read "replacement_needed.txt" file. This file has one
mistake. One letter needs to be replaced with other letter then this
sentence might have some meaning. Replace this letter with the desired
one making logic yourself without using any library. Write your code in
function and call that function. Handle all possible exceptions as well.
'''

def correct_letter_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        print(f"Original content: {content}")

        if 'z' in content:
            corrected_content = content.replace('z', 's')
            print(f"Corrected content: {corrected_content}")

            with open(file_path, 'w') as file:
                file.write(corrected_content)

            print("File has been updated with corrected content.")
        else:
            print("No 'z' found in the content. No changes needed.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read/write the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_name = "replacement_needed.txt"
correct_letter_in_file(file_name)