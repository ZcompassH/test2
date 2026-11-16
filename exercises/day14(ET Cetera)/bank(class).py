class Account:
    def __init__(self):
        self._balance = 0#加下划线是避免属性名和实例变量冲突，_表示为私有变量。虽然python不强制似有性

    @property
    def balance(self):  #设置的Geeter，但没有设置Setter
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(25)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

#constants， 常量变量，很难修改