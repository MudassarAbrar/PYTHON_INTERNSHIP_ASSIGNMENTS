'''
1. Write a Python program that includes three separate functions to:
 Calculate the area of a trapezoid
 Calculate the area of a parallelogram
 Calculate the surface area and volume of a cylinder
 Each function should take the necessary arguments and if user select Area for
trapezoid then It should be print.

'''
from math import pi
def area_of_trapezoid(b1,b2,h):
    return (0.5*(b1+b2)*h)


def area_of_parallelogram(b,h):
    return (b*h)


def surface_area_of_cylinder(r,h):
    
    return (2*pi*(r**2)+2*pi*r*h)

def volume_of_cylinder(r,h):
    return (pi*(r**2)*h)

def input_taking_func():
    while True:
        print("\nSelect an option:")
        print("1. Calculate the area of a trapezoid")
        print("2. Calculate the area of a parallelogram")
        print("3. Calculate the surface area of a cylinder")
        print("4. Calculate the volume of a cylinder")
        print("5. Exit")
        
        option = int(input("Enter your choice (1-5): "))
        
        if option == 1:
            base1 = float(input("Enter the value of Base-01: "))
            base2 = float(input("Enter the value of Base-02: "))
            height = float(input("Enter the value of Height: "))
            print(f"Area of Trapezoid: {area_of_trapezoid(base1, base2, height):.2f}")
        elif option == 2:
            base = float(input("Enter the value of Base: "))
            height = float(input("Enter the value of Height: "))
            print(f"Area of Parallelogram: {area_of_parallelogram(base, height):.2f}")
        elif option == 3:
            radius = float(input("Enter the Radius value: "))
            height = float(input("Enter the Height value: "))
            print(f"Surface Area of Cylinder: {surface_area_of_cylinder(radius, height):.2f}")
        elif option == 4:
            radius = float(input("Enter the Radius value: "))
            height = float(input("Enter the Height value: "))
            print(f"Volume of Cylinder: {volume_of_cylinder(radius, height):.2f}")
        elif option == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


input_taking_func()