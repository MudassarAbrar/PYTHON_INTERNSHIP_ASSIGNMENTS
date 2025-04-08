'''
6. Create a class called "Employee" with properties "name" and "salary".
Add a method called "calculateBonus" that calculates a bonus amount
based on the employee's salary. Managers get a bonus equal to 20% of
their salary, while developers get a bonus equal to 10% of their salary.
Then, create two subclasses called "Manager" and "Developer" that

inherit from the Employee class. The Manager class should have a
method called "hire" that logs a message indicating that the manager is
hiring someone, while the Developer class should have a method called
"writeCode" that logs a message indicating that the developer is writing
code. Finally, create a subclass called "SeniorManager" that inherits
from the Manager class and that should have the "calculateBonus"
method to give senior managers a bonus equal to 30% of their salary.

'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        
    def calculateBonus(self):
         pass
        
class Manager(Employee):
    def hire(self):
        return f"{self.name} is hiring someone."
    
    def calculateBonus(self):
        return 0.20 * self.salary
    
    
class Developer(Employee):
    def writeCode(self):
        return f"{self.name} is writing code."
    
class SeniorManager(Manager):
    def calculateBonus(self):
        return 0.30 * self.salary
    
    
    
    

manager = Manager("Alice", 50000)
developer = Developer("Bob", 40000)
senior_manager = SeniorManager("Charlie", 70000)

print(f"{manager.name} Bonus: ${manager.calculateBonus()}") 
print(f"{developer.name} Bonus: ${developer.calculateBonus()}") 
print(f"{senior_manager.name} Bonus: ${senior_manager.calculateBonus()}") 

print(manager.hire()) 
print(developer.writeCode())