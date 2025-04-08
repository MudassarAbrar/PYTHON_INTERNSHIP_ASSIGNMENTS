'''
Write a program in which a class named Account has private member
variables named account_no ,account_bal ,security_code. Use a public
function to initialize the variables and print all data.

'''


class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code
        
    def setter(self, account_no, account_bal, security_code):
    
        self.__account_no = account_no
        if account_bal < 0:
            raise ValueError("Account balance cannot be negative.")
        self.__account_bal = account_bal
        self.__security_code = security_code
        
        
    def getter(self):
        return f"Account No: {self.__account_no}, Account Balance: {self.__account_bal}, Security Code: {self.__security_code}"
    
    
    def initialize_and_print(self, account_no, account_bal, security_code):
        self.setter(account_no, account_bal, security_code)
        print(self.getter())
        
        
        
try:  
        
    account = Account("123456789", 1000, "ABC123")
    print(account.getter())  
    account.initialize_and_print("987654321", 2000, "XYZ789")
    
    
except ValueError as e:
    print(f"Error: {e}")