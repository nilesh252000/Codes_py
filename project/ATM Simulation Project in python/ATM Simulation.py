class ATM:
    def __init__(self,balance):
         self.balance=balance
    def check_balance(self):
        return self.balance
    def deposite(self,amount):
        self.balance+=amount
        return self.balance
    def withraw(self,withraw):
        self.balance-=withraw
        return self.balance

balance=1000
atm_obj=ATM(balance)
password=input("Enter The Password :")
while True:
    if password=="1234":
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        choise=input("Enter the choise  ")
        if(choise=="1"):
            result=atm_obj.check_balance()
            print("Available balance",result)
        elif(choise=="2"):
            amt = int(input("Press amount to deposite youracco"))
            result=atm_obj.deposite(amt)
            print("Avau=ilable balance :", result)
        elif(choise=="3"):
            withrawl=int(input("Enter the withrawl amount"))
            result=atm_obj.withraw(withrawl)
            print("Avau=ilable balance :", result)
            break


