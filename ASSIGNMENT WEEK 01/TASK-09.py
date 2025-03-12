'''

Write a python program that take 5 subjects marks from the user and then check the
condition if input marks > 100 then show the output " Invalid Input", if input marks >=
50 but <= 100 then show " Pass" otherwise show "Fail".

'''


for x in range(1,6):
    marks = int (input(f"ENTER THE MARKS FOR SUBJECT {x}:  "))
    
    if marks > 100:
        print("IVALID MARKS!!! Marks can't be greater than 100 ")
    elif marks >= 50 and marks<=100:
        print("PASS!!")
    else: 
        print("FAIL!!!")