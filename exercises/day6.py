# 异常

#自己写的代码给用户玩，用户的输入是随机的，可能会造成异常，因此可以提前写入对应的防御性代码。


#补充说明：主函数里get_number()括号里的内容叫“实参”，他是调用这个函数时参数的实际值。
          #而定义函数时，即def get_number():时，括号里的是“形参”，表示该函数至少需要输入一个参数，
          #定义函数和调用函数时，括号里的参数量需要相同才行。规则：调用时给的实参个数，必须和定义时的形参个数对得上。
                                    #除非有默认值，即def get_number(prompt=5),这就是默认值，不算入参数个数

def main():
    x = get_number("what's x?")  #括号里的实参是给prompt的实际值
    print(f"x is {x}")
    age = get_number("how old are you?")
    print(age)

def get_number(prompt): 
    while True:
        try:   #如果现try再while true，那么在int炸了之后会直接跳出，因为try只尝试一次
            
    #这里的prompt就变成了主函数里的实参"what's x?",然后input把实参变成输入值，交给int转换
            return int(input(prompt)) #可以简化成 return  int(input("what's x?")),,,,return带有break的跳出属性，可以做到跳出和返回捅同时执行
        except ValueError:
            print("x is not an integer") 
            pass  #pass表示什么都不输入，如果没有上面的print，pass会让代码直接循环到"what's x?"
                  #pass 唯一的作用是：语法要求这里必须有个语句，但你确实没东西要写。
main()


# while True:
#     x = int(input("what's x ?"))
#     return x                        return只能用到函数里，这里是一个错误点
    
# print("x is",x)