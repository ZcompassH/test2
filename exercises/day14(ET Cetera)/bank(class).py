class Account:
    def __init__(self):
        self._balance = 0#加下划线是避免和 property 的方法名 balance 冲突，_表示为私有变量。虽然python不强制似有性

    @property
    def balance(self):  #设置的Geeter，但没有设置Setter。Geeter只能看、读，不能写
        return self._balance

    def deposit(self, n):
        self._balance += n  #_balance 才是存数据的地方；balance 只是只读窗口，不能赋值
#_balance 是唯一的存储位置，balance 只是读它的入口。 所以任何"改"，最终都必须落到 _balance 上——哪怕是在 setter 里面。
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