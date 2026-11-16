balance = 0#全局变量，一般来说全局变量不可改变

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(25)
    print("Balance:", balance)

def deposit(n):
    global balance#加上这一句，就是告诉python这是一个全局变量，这样就可以更改变量的数值
    balance += n

def withdraw(n):    #顺带一提，如果在局部设定一个与全局变量同名的变量，python会识别并在局部使用局部变量，不会改变global。即局部遮盖全局
    global balance
    balance -= n

if __name__ == "__main__":
    main()