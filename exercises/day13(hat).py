import random

class Hat:
    #类变量存在与类本身内部，这个变量只有一个副本，共该类所有对象使用
    houses = ["hubei", "shanxi", "heilongjiang", "shandong"]#类变量，不在调用self

    @classmethod#类方法，是一个decorator装饰器
    def sort(cls,name):#写成cls是为了避免重名造成冲突，也是约定俗成的。
        print(name, "is in", random.choice(cls.houses))


Hat.sort("zh")#删掉了hat = Hat将类转换成实例变量的这一步，这就是类方法，不需要实例变量来接收存储