'''

Write a program to make a simple console based calculator performing the four basic
operations (+, -, *, /) on two numbers input by user.Your program should ask the user
which operation he/she wants to perform and gives the output accordingly.

'''

functions = ["ADDITION", "SUBTRACTION", "MULTIPLICATION", "DIVISION"]


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


def main():
   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Which operation do you want to perform?")
    for x, y in enumerate(functions):
        print(f"{x + 1}: {y}")
    while True:
    
        choice = int(input("Enter the number corresponding to the operation: "))

    
        if choice == 1:
            print(f"Result: {addition(num1, num2)}")
            break
        elif choice == 2:
            print(f"Result: {subtraction(num1, num2)}")
            break
        elif choice == 3:
            print(f"Result: {multiplication(num1, num2)}")
            break
        elif choice == 4:
            print(f"Result: {division(num1, num2)}")
            break
        else:
            print("Invalid choice. Please select a valid operation.")


if __name__ == "__main__":
    main()
