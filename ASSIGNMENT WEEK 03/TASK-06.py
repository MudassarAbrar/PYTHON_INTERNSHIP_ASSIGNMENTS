'''
Create a function that asks the user to enter a sentence then writes the
sentence to a text file named "questions.txt" if it's a question. Handle all
possible exceptions as well.

'''


def write_question_to_file():
    try:
        sentence = input("Enter a sentence: ").strip()
        if sentence.endswith("?"):
            try:
                with open("questions.txt", "a") as file:
                    file.write(sentence + "\n")
                print("The question has been written to 'questions.txt'.")
            except IOError as e:
                print(f"An error occurred while writing to the file: {e}")
        else:
            print("The entered sentence is not a question.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

write_question_to_file()
