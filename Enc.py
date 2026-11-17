class Atm:
    def __init__(self):
        self.balance=0
        self.pin=""

        self.menu()
    def menu(self):
       user_Input=input('''
        1.1 to create pin
        2.2 for check balance
        3.3 for deposit
        4.4 for withdraw
        ''')

       if user_Input=="1":
        print("create pin")
        self.create_pin()
       elif user_Input=="2":
        print("check balance") 
        self.check_balance() 

       elif user_Input=="3":
        print("deposit")
        self.make_deposit()  

       elif user_Input=="4":
        print("withdraw")
        self.make_withdraw()

       else:
        print('wrong pin')

    def create_pin(self):
        temp=input("enter the pin")
        self.pin=temp
        if self.pin!='':
            print("print created successfully")


    def check_balance(self):
        temp=input("enter the pin")
        if temp==self.pin:
            print(f"your balance is {self.balance}")      

    def make_deposit(self):
        temp=input("enter the pin")
        if temp==self.pin:
            amt=int(input("enter the amt"))
            if amt <=0:
                print("please enter valid amt")
            else:
                print("amt is valid")
                print(f"your balance is {self.balance}")     
                self.balance +=amt  
                print(f"your balance after deposit is {self.balance}")    
        else:
            print("invalid")

    def make_withdraw(self):
        temp=input("enter the pin")
        if temp==self.pin:
            amt=int(input("enter the amt"))
            if amt>self.balance:
                print("insufficient balnce")

            else:
                self.balance-=amt
                print(f"your balance after withdraw is {self.balance}") 
                    
