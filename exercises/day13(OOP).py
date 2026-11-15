#今天继续学OOP，面向对象编程
#raise可以让操作者主动抛出异常，而并非python自动生成的异常。用来检测我们需要的内容
class Student:
    def __init__(self,name,house):
        if not name:#python的写法，也可以写成if name == “”
            raise ValueError("Missing name")#主动抛出异常，并在python里可以把所有异常错误类型当成函数，在里面添加详细的信息来报错，方便阅读
        self.name = name
        self.house = house

    def __str__(self): #可以把print打印的隐晦信息转换成字符串，使其可读
        return f"{self.name} from {self.house}"
#Geeter获取器,获取属性值的函数
    @property #将下面的函数设成Geeter
    def house(self):
        return self._house#这里的_是为了避免与init里的self.house冲突的默认写法
#Setter设置器，设置属性值的函数
    @house.setter  #将下面的函数设成Setter，且这里的名字与Geeter相同，是因为创建Geeter后自动生成的Setter
    def house(self,house):#将Setter的名字设置成属性名即house，此时所有带.house的变量都需要来Setter里验证一遍是否可以操作，包括init函数
        if house not in ["hubei", "shanxi", "shandong", "heilongjiang"]:
            raise ValueError("Ivalid house") 
        self._house = house#这样设置后可以防止程序被恶意篡改，如果想在main里改self.house都会经过Setter的验证是否通过
#真的能防止吗？改不了self.house,但可以改self._house。
    #python设计的目的就是这种可见性，没有真正的可以防止修改内容的方式，python并不想要强制要求
    # python里的self._house（也可以写成self.__house）本质是一种君子约定，告诉别人不要修改这里，起到强调作用
#其实int、str、list、dict都是class（类），里面都内置了很多method，如list.lower来强制小写             
def main():
    student = get__student()
    print(student) #def了__str__之后，打印出来的内容会变成想要的字符串形式

def get__student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    
    
if __name__ == "__main__":
    main()

#properties更具防御性的attribute     decorators装饰器
#@property语法


#@classmethod  类方法，不同于实例变量。它不定义一种新的区分与其他method，而是取相同点