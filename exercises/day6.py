# 异常

#自己写的代码给用户玩，用户的输入是随机的，可能会造成异常，因此可以提前写入对应的防御性代码。

def main():
    x = get_number()
    print(f"x is {x}")

def get_number():
    while True:
        try:                #如果现try再while true，那么在int炸了之后会直接跳出，因为try只尝试一次
            x = int(input("what's x?"))
            return x   #可以简化成 return  int(input("what's x?")),,,,return带有break的跳出属性，可以做到跳出和返回捅同时执行
        except ValueError:
            print ("x is not an integer")   
            pass  #pass表示什么都不输入，如果没有上面的print，pass会让代码直接循环到"what's x?"

main()


# while True:
#     x = int(input("what's x ?"))
#     return x                        return只能用到函数里，这里是一个错误点
    
# print("x is",x)