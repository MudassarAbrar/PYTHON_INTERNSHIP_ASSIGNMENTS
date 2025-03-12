'''
Write a program to take marks of 3 subjects as input by user and store them in a
dictionary having appropriate keys. Using that dictionary calculate average and
percentage of those marks.

'''

std_data = {}

subjects = ["ENGLISH","MATH","PHYSICS"]


for subject in subjects:
    std_data[subject] = int(input(f"ENTER {subject} MARKS: "))
    
    
    
total_marks = sum(std_data.values())

average_marks = total_marks / len(subjects)
    
    
max_marks_per_subject = 100
percentage = (total_marks / (max_marks_per_subject * len(subjects))) * 100

print("\nStudent Marks:")
for subject, marks in std_data.items():
    print(f"{subject}: {marks}")

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
    
    
