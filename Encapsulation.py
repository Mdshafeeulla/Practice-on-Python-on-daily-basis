class BankAccount:
    def __init__(self, name : str, balance = 0):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount <= 0:
            print("Please insert amount greater than zero rupees")
        else:
            self.__balance += amount
    def withdrawal(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def balance(self):
        print(f"The remaining balance is {self.__balance} for {self.name} ")

shafi = BankAccount("shafi")
shafi.deposit(500)
shafi.balance()

shafi.withdrawal(500)
shafi.balance()