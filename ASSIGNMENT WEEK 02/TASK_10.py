'''
10. An online shopping platform wants to calculate the total bill for a customer, including a
discount. The discount is applied based on the total purchase amount.
 If the total amount is above $500, a 10% discount is applied.
 If the total amount is above $1000, a 20% discount is applied.
Write a Python function that takes the total purchase amount as an argument and
returns the final bill after applying the discount. Explain why using a function makes the
code more efficient.
'''
def functions_role():
    print("Functions make the code more reuseable , modular , efficient , easy to handle and consise")
def bill_generator(amount):
    try:
        if amount < 0:
            raise ValueError("AMOUNT CAN'T BE NEGATIVE")
        elif amount <= 500:
            return f"Sorry! You can't get a discount at ${amount}. Shop more to qualify for discounts. ;)"
        elif 500 < amount <= 1000:
            return f"The final bill after a 10% discount is: ${amount - (amount * 0.1):.2f}"
        else:
            return f"The final bill after a 20% discount is: ${amount - (amount * 0.2):.2f}"
        
        
    except ValueError as e:
        print(f"ERROR: {e}")
    
    
    
total_amount = int(input("ENTER THE TOTAL PURCHASE AMOUNT:  "))


print(bill_generator(total_amount))
print("<-------------------------------------------------------------------------->")
functions_role()
        