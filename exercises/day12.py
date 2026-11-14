#面向对向编程 OOP
#tuple  元组，类似list，但不用加[]，用逗号分隔即可，且不可修改
#例： name,house = get_student  name，house就是一个元组b
#tuple、 list、 dictionary，不同的通用数据类型，这里介绍另一种--classes，类，像是数据对象的蓝图，可以自定义
#类是新数据的定义，对象(object)是类的“具体化”，或者说是“实例化”
class Student: #定义一个类，只要定义了类，就会自动得到一个同名的函数。且类里面不仅可以创建很多属性，还可以添加很多method，函数
    def __init__(self, name, house): #__init__实例方法，想初始化类的对象内容，就得定义这个method，self是自带的隐含的辅助参数
        #self可以任意写，跟随的变量也是，比如这里写成self.n   self.h
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")#用点语法给类添加属性（attributes）  实例变量(instance variables)
    student.house = input("House: ") #name,house本质是这个类内部的实例变量
    return student

if __name__ == "__main__":
    main()
#11.14,今天看到50min，明天继续。
