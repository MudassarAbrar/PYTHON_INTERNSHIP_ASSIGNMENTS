'''
Take two integer numbers from user as input. Divide these two numbers.
If one number is being divided by zero (another number) then handle
ZeroDivisionError and if entered value is wrong (for example, a string)
then handle ValueError.


'''


def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter valid integer numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

divide_numbers()
