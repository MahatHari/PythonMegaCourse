# base class
class Account():
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as f:
            self.balance = int(f.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


# sub class
class Checking(Account):
    """This class generates checking account objects """

    type = "checking"

    # constructor
    def __init__(self, filepath, fee):
        # inheritance
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount-self.fee


checking = Checking("balance.txt", 1)
checking.deposit(10)


print(checking.balance)
checking.withdraw(100)
print(checking.balance)
checking.deposit(200)
print(checking.balance)

checking.transfer(20)
print(checking.balance)
checking.commit()

print(checking.type)
print(checking.__doc__)
