class user_bank_account:
    
    def __init__(self,name,card_no,pin):
        self.card_number = card_no
        self.name = name
        self.pin = pin 
        self.balance = 0 
    
    def display_current_balance(self):
        print('Current Bank Balance is : Rs. ',self.balance)
        
    def update_pin(self,pin):
        self.pin = pin 
        print('Your ATM pin has been updated successfully ! ')
    
    def add_money(self,amount):
        self.balance += amount
        print('Amount is added to your bank account successfully !',)
        print('Current balace is : Rs. ',self.balance) 
        
    def withdraw(self,amount):
        pss = input ("Enter the pin : ")
        if int(pss)==self.pin:
            if self.balance >= amount:
                self.balance -= amount
                print('Amount has been debited by Rs. ', amount ,'from your bank account !')    
            else:
                print('Insufficient Balance ! ')
                print('Current balace is : Rs. ',self.balance)
        else:
            print ("Invalid pin!!!")
    

print('Insert the following details ')
name = input('Enter Name : ') 
card_no = int(input('Enter the last 4 digits of credit card : ')) 
pin = int(input('Enter the 4 digit ATM pin : '))

user_1 = user_bank_account(name,card_no,pin)
print()

while True:
    
    print('1. To check the current bank balance \n2. To Add money \n3. To withdraw money  \n4. To update your ATM pin \n5. Exit')
    print()
    choice = int(input('Enter your choice : '))
    print()
    if choice == 1:
        user_1.display_current_balance()
        print()
        
    elif choice == 2:
        money = int(input('Enter the money you want to debit : '))
        user_1.add_money(money)
        print()
        
    elif choice == 3:
        money = int(input('Enter the money you want to withdraw : '))
        user_1.withdraw(money)
        print()
        
    elif choice == 4:
        pin = int(input('Enter the new 4 digit ATM pin : '))
        user_1.update_pin(pin)
        print()
    
    elif choice == 5:
        print('Exited..!')
        print()
        break
    
    else:
        print('Enter a valid choice ')        
        print()        
