'''
Take biodata of employee from user as Name, cnic number, age, and
salary save it in txt file. Now append this file to add contact number.
Finally read this file. Handle all possible exceptions as well.
'''

def write_biodata_to_file(name, cnic, age, salary, contact_number):
    try:
        with open("biodata.txt", "w") as file:
            file.write(f"Name: {name}\n")
            file.write(f"CNIC: {cnic}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Salary: {salary}\n")
            print("The biodata has been written to the file successfully.")
            
        with open("biodata.txt", "a") as file:
            file.write(f"Contact Number: {contact_number}\n")
            print("The contact number has been appended to the file successfully.")
            
        with open("biodata.txt", "r") as file:
            content = file.read()
            print("The content of the file is:")
            print(content)
    except IOError as e:
        print(f"File operation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during file handling: {e}")
        
        
        
def main():
    try:
        name = input("Enter the name of the employee: ")
        cnic = input("Enter the CNIC number of the employee: ")
        age = input("Enter the age of the employee: ")
        salary = input("Enter the salary of the employee: ")
        contact_number = input("Enter the contact number of the employee: ")

        write_biodata_to_file(name, cnic, age, salary, contact_number)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
        
if __name__ == "__main__":
    main()