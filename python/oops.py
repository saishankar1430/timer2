class HdfcBank:
    ifscCode = "A3OB3B5D9"
    Branch = "Medchal"
    def __init__(self, name,id, pNo):
        self.account_name = name
        self.id = id
        self.phoneNo = pNo
        self.atmPin = -1
        self.balance = 0
        self.account_No = pNo % 100000 + 8011
        self.otp = 1234
        print("your account is created succesfully, your account number is ", self.account_No)
    def deposit(self):
        accNo = int(input("enter your acc number"))
        if accNo == self.account_No:
            m = int(input("enter the amount to deposit"))
            self.balance += m
            print(f"your account balance is {self.balance}")
        else:
            print("no account found with this acc no")
    def showBalance(self):
        print("Account balace is",self.balance)
    def setAtmpin(self):
        accNo = int(input("enter your acc no"))
        if self.account_No == accNo:
            phno = int(input("enter your phone number"))
            if phno == self.phoneNo :
                print("an otp has been sent to your phone number")
                otp = int(input("enter the 4 digit otp"))
                if otp == self.otp :
                    pin = int(input("enter your 4 digit atm pin"))
                    pin2 = int(input("enter your atm pin again"))
                    if pin == pin2:
                     self.atmPin = pin
                     print("atm pin set successfully")
                    else:
                     print("please enter same atm pins")
                else:
                    print("please enter correct otp")
            else:
                print("enter correct phone number")
        else:
            print("Incorrect account number")
        
acc1 = HdfcBank("Shubham", 148824863453, 9849568112)

acc1.deposit()
acc1.setAtmpin()
acc1.showBalance()
