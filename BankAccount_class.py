class BankAccount:
    
    
    def __init__(self , accountnumber,name,balance ):
       
       self.accountnumber = accountnumber
       self.name = name 
       self.balance = balance
    
    
    def  Deposite(self ,amount):
        
        self.balance = self.balance + amount
        
        return print(f"Deposited: {amount}. New balance: {self.balance}")
    def  Withdrawal(self ,amount):
        
        self.balance = self.balance - amount
        
        return print(f"Withdrawal: {amount}. New balance: {self.balance}")
    def  bankfees(self ):
        
        fees = int(self.balance * 0.05)
        self.balance = self.balance - fees
        
        return print(f"Fee: {fees}. New balance: {self.balance}")
        
    def display(self):
        print(f'Account Number : {self.accountnumber}')
        print(f'Account Name : {self.name}')
        print(f'Account Balance : {self.balance}')
    
    
        
newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(1000)          
newAccount.Deposite(1400)          
newAccount.bankfees()
newAccount.display()          