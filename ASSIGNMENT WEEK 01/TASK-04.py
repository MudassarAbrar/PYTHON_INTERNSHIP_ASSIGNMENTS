'''
Write a program that returns the sum of all the elements in the given list of task 3.


'''
def main():
   
    numbers = [2, 4, 6, 5, 3, 8, 2, 6, 6, 4]

# Using the built-in sum function
    def sum_function(x):
        return sum(x)

    print("Sum using built-in sum function:")
    print(sum_function(numbers))

    print("========================")
# other approach
    total = 0
    for num in numbers:
        total += num

    print("Sum using a loop:")
    print(total)

if __name__ == "__main__":
    main()
