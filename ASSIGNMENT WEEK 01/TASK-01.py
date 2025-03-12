'''
1. Calculate the body mass index (BMI) of two variables input by the user.
BMI Calculation Formula = weight/ (height)^2.

'''
def body_mass_index(w, h):
    return w / (h ** 2)

try:
    user_weight = float(input("Enter your weight in kilograms: "))
    user_height = float(input("Enter your height in meters: "))
    
    if user_weight <= 0 or user_height <= 0:
        print("Weight and height must be positive values.")
    else:
       
        bmi = body_mass_index(user_weight, user_height)
        print(f"Your BMI is: {bmi:.2f}")
        
      
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
except ValueError:
    print("Please enter valid numeric values for weight and height.")
