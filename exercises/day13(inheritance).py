class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...


class Student(Wizard):#inheritance，遗传、继承   类可以继承父类的变量功能
    def __init__(self, name, house):#初始化自己的变量，可以和父类有相同点，只要在下面继承即可
        super().__init__(name)#继承父类Wizard的name变量
        self.house = house#并创建自己的实例变量
    ...

class Professor(Wizard):#像这样，类与类之间可以创建层级联系，这些类的共同点可以通过父类向下传递。
    def __init__(self, name, subject):          #存在父类，祖父类这种关系，
        super().__init__(name)                  #其实异常错误也是有层级关系的类，这么设计的目的是这些异常类型都有很多共同点
        self.subject = subject
    ...



##运算符重载 operator overloding
class Vault:#金库
    def __init__(self,yuan=0, jiao=0, fen=0):
        self.yuan = yuan
        self.jiao = jiao
        self.fen = fen

    def __str__(self):
        return f"{self.yuan} yuan, {self.jiao} jiao, {self.fen} fen"

    def __add__(self, other):#other也是默认规定，可以改
        yuan = self.yuan + other.yuan
        jiao = self.jiao + other.jiao#这里的元角分其实用复数来区分更清晰，但实际只是局部的变量，不会冲突
        fen = self.fen + other.fen
        return Vault(yuan, jiao, fen)

zh = Vault(100,50,25)
print(zh)

ljl = Vault(50,100,25)
print(ljl)
#现在要实现直接zh + ljl ，所以要让python理解我们现在+的意思
total = zh + ljl #通过__add__  ,可以实现两个实例的相加，因为我们补充的+的定义、用法
print(total)