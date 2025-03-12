'''
3. Write a program to make function employee() meeting following requirements:
Employee name and monthly salary will be passed to this function. This function will cut
2 percent tax from salary and display salary after tax with name of employee. If the
salary is missing in the function call then assign default value 10,000 to salary.
'''


def employee(name,salary =10000):
    return f"Employee: {name}, Salary after 2% tax: {(salary - salary*0.02):.2f}"




name = input("ENTER THE EMPLOYEE'S NAME: ")

salary_input = input("ENTER THE EMPLOYEE'S SALARY (leave blank for default 10,000): ")
if salary_input.strip(): 
    salary = int(salary_input)
else:
    salary = 10000
    
    
print(employee(name,salary))