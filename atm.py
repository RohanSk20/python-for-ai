class bank:
    def __init__(self, balance,password):
        self.balance = balance
        self.__password = password

    #set pin

    def pin(self):
        newpin = int(input("set new pin"))
        self.__password= newpin
        print("PIN updated successfully ")


      #deposit amount 
        
    def deposit(self,amt):
        pincode=int(input("enter pin \n"))
        if(pincode != self.__password):
            print("invalid pin")
            return

        self.balance += amt
        print(f"amount added successfully \n available balance= {self.balance}")
    
    #check balance

    def checkbalance(self):
        print(f"{self.balance}")

    #withdrawl amount 

    def withdraw(self, amt):
        pincode=int(input("enter pin \n"))
        if(pincode != self.__password):
            print("invalid pin")
            return
        
        if(amt>self.balance):
            print("low balance")
        else:
            self.balance -= amt
            print(f"{amt} withdrawn successfully \n current balance is {self.balance}")

mover = bank(balance=0,password=0000)
print("welcome to new bank--- \n")
while True:
    print("----------------------")
    print("enter your choice: \n")
    choice = int(input( "\n Check balance (1) \t create new pin (2) \n depost amount(3) \t withdraw amount (4): \n you choice="))
    print("----------------------")
    if(choice == 1):
        mover.checkbalance()
    elif(choice == 2):
        mover.pin()
    elif(choice == 3):
        amt = int(input("enter deposit amount "))
        mover.deposit(amt)
    elif(choice == 4):
        amt = int(input("enter deposit amount "))
        mover.withdraw(amt)
    