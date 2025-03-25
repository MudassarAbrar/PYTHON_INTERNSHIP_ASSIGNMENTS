'''
5. Take input from user below dictionary having name and age pair. Save
this dictionary in json file. Now load this json file and Print name of
person having maximum age and also print if anyone has the same age
by making logic yourself without using any library

dictionary = {'Ali':
23,'Saad':24,'Salman':15,'Shams':25,'Sadiq':46,'Hammad':23'} Handle all
possible exceptions as well.

'''

def write_dict_to_json(dictionary):
    try:
        with open("dictionary.json", "w") as file:
            file.write(str(dictionary))
            print("The dictionary has been written to the file successfully.")
            
        
    except IOError as e:
        print(f"File operation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during file handling: {e}")
        
        
def load_from_json_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
           
            dictionary = eval(content)
            return dictionary
    except IOError as e:
        print(f"File operation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
    
def find_max_age(dictionary):
    try:
        max_age = -1
        persons_with_max_age = []

        for name, age in dictionary.items():
            if age > max_age:
                max_age = age
                persons_with_max_age = [name]
            elif age == max_age:
                persons_with_max_age.append(name)

        print(f"The person(s) with the maximum age ({max_age}) is/are:")
        print(", ".join(persons_with_max_age))
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")



if __name__ == "__main__":
    dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
    write_dict_to_json(dictionary)
    
    dictionary = load_from_json_file("dictionary.json")
    if dictionary:
        find_max_age(dictionary)
    else:
        print("An error occurred while loading the dictionary from the file.")