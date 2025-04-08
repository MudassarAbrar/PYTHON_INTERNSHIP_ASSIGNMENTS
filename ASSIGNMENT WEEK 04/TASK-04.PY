'''
4. A university is deciding to upgrade its system. In order to upgrade, you
need to implement the following scenario:

Note the following,
• The class student has a function that displays information about the
student i.e. id and name.
• Class marks is derived from class student and has a function that
displays all the marks obtained in the courses by the students. i.e.
marks_algo, marks_dataScience, marks_calculus.
• Class result is derived from class marks. This class has a function that
calculates the total marks and then calculates the average marks. It
then displays both the total and the average marks.
In the main function you are required to do the following:
• Create an object of the result class.
• Then display the student details, the marks obtained in each courses
and the total and the average marks.

'''

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        
    def display_info(self):
        return f"Student ID: {self.student_id}, Name: {self.name}"
    
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}"
    
    
class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus
        
    def display_marks(self):
        return f"Marks in Algorithm: {self.marks_algo}, Marks in Data Science: {self.marks_dataScience}, Marks in Calculus: {self.marks_calculus}"
    
    def __str__(self):
        return f"{super().__str__()}, Marks in Algorithm: {self.marks_algo}, Marks in Data Science: {self.marks_dataScience}, Marks in Calculus: {self.marks_calculus}"
    
    
    
class Result(Marks):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name, marks_algo, marks_dataScience, marks_calculus)
        
    def calculate_total(self):
        return self.marks_algo + self.marks_dataScience + self.marks_calculus
    
    def calculate_average(self):
        total_marks = self.calculate_total()
        return f"{(total_marks / 3):.2f}"
    
    def display_result(self):
        total_marks = self.calculate_total()
        average_marks = self.calculate_average()
        return f"Total Marks: {total_marks}, Average Marks: {average_marks}"
    
    
    
def main():
    student_id = "S12345"
    name = "Mudassir Abrar"   
    marks_algo = 85
    marks_dataScience = 90  
    marks_calculus = 78
    
    result = Result(student_id, name, marks_algo, marks_dataScience, marks_calculus)
    
    print(result.display_info())
    print(result.display_marks())
    print(result.display_result())
    
    
    
if __name__ == "__main__":
    main()
    