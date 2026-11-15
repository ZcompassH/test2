#今天继续学OOP，面向对象编程
#raise可以让操作者主动抛出异常，而并非python自动生成的异常。用来检测我们需要的内容
class Student:
    def __init__(self,name,house):
        if not name:#python的写法，也可以写成if name == “”
            raise ValueError("Missing name")#主动抛出异常，并在python里可以把所有异常错误类型当成函数，在里面添加详细的信息来报错，方便阅读
        if house not in ["hubei", "shanxi", "shandong", "heilongjiang"]:
            raise ValueError("Ivalid house")
        self.name = name
        self.house = house

def main():
    student = get__student()
    print(f"{student.name} from {student.house}")

def get__student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    
    
if __name__ == "__main__":
    main()