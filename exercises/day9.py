#morning

#file I/O


#在之前的函数中，只是一些简单的一次性互动，需要用户每次输入参数值来运行，
# 且每次都会重置，无法记录、保存我们输入，计算后的结果
# name = input("what's your name?")
# print(f"hello",name)

#介绍open函数
#open():   #它可以打开或创建文件，并对文件进行编辑输入输出

name = input("waht's your name?")

file = open("names.txt","w") #译为，打开（没有就创建）names.txt这个文件，“w“为write缩写，即可以编写
file.write(name)    #译为，将name写入文件
file.close()       #关闭文件
# #上述写法会有问题，"w"会导致每次重新运行时，会覆盖文件之前保存的内容。每次打开都会重新创建并写入

# #解决方式只要把"w"改成"a"即可，a即append，译为追加，会在文件末尾追加这次的输入
file = open("names.txt","a") 
# file.write(name)    #但这样会导致每次输入的内容首尾相连，因此需要换行
file.write(f"{name}\n")  #这样就可以每次输入是单独一行了，当然，方法多样
file.close()

#with语句，为避免程序员忘记写close函数来关闭文件，造成文件损坏或丢失
#with  open(...)  as  变量名，这是with语句的固定搭配
with open("names.txt","a") as file:
    file.write(f"{name}\n")#效果如此，在写入之后，或open结束后，会自动关闭文件

#已经用上述语句写入了三个名字，现在介绍"r"即read，读取模式
with open("names.txt","r") as file: 
    lines = file.readlines() #readlines函数就可以读取文件中的每一行数据

for line in lines:
    print("hello,",line.rstrip())#rstrip()函数可以去除每一行末尾的换行符，
#     #不然这里print再创建一个换行符就会两次换行，或者用end=    去除print的\n也可以

# #简洁写法
with open("names.txt","r") as file:
    for line in file:
        print("hello,",line.rstrip())
#怎么实现每次读取打印，可以自动按字母顺序来排序呢？
names = [] #创建list

with open("names.txt")as file: #open默认是r模式，用r模式可以不写
#     for line in file:
#         names.append(line.rstrip())#这里append是在list里追加存量，在file里循环追加

# for name in sorted(names):#sorted是排序函数，按字母排序
#     print(f"hello,{name}")
#为什么不直接排序file？
    for line in sorted(file):
        print("hello,",line.rstrip())

#逗号分隔值文件，csv   CSV（Comma-Separated Values，逗号分隔值）
with open("students.csv") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")
#split(，)函数，可以分割scv文件的每一行用逗号隔开的存量，然后组成一个list，最后可以用row[0]这样来引用
#注意事项：
#由于文件读出来最后都会带\n，所以永远是 line.strip().split(",")，先去掉首尾空白和换行。
#split出来都是字符串，"11"是字符串不是数字
#引号里的逗号也会被拆
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")#如果提前知道file里一行是两个存量，可以提前定义这两个存量，然后直接调用
        #这样写比row[0]要更加直接，清晰


students = []
with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = {"name": name, "house":house}#创建字典，并关联
        students.append(student)

def get_name(student):
    return student["name"]
                                  #key是sorted里用来特定排序的功能，可单独按照get_name的返回值来排序，这里函数不加括号()
for student in sorted(students, key=get_name ,reverse=True):#reverse=True可以反向排序，默认值为Flase，更改后即可反向排序
    print(f"{student['name']} is in {student['house']}")
#上述代码里，定义的get_name()后立刻就使用且只用一次，因此可省略
for student in sorted(students, key=lambda student: students["name"]):#sorted会自动调用key=的函数
    print(f"{student['name']} is in {student['house']}")
#lambda是匿名函数，用在这种只需要调用一次的函数时，避免反复定义这种一次性函数，

def get_name(s):
    return s["name"]
# 上面这两行，和下面这一行是同一个东西
get_name = lambda s: s["name"]#lambda在定义时不用加（），调用时才用



#  encoding=... 可以避免文件里有中文造成的报错
with open("students.csv", encoding="utf-8") as file:
    next(file)          # 跳过表头
    for line in file:
        ...         

#csv里有现成的函数去处理csv文件，比spilt更加智能
import csv #a mudual
students = []#创建list
with open("exercises/students.csv") as file:
    reader = csv.reader(file)#csv.reader可以查看并处理.csv文件
#提取文件里用逗号分隔的存量，并且会识别一些不应该被分隔，但带有逗号的存量
    for name,home in reader:
        students.append({"name": name,"home":home})
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']}is from {student['home']}")

    #经过漫长的理解，终于进入最后的DictReader
    #reader会把每行的文本加载成列的列表，而DictReader会加载成列的字典

import csv #a mudual
students = []#创建list
with open("exercises/students.csv") as file:
    reader = csv.Dictreader(file)
    for row in reader:
        students.append({"name": row["name"],"home":row["home"]})
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
#reader认索引，因为是list，而DictDReader认名字，因为是字典，不怕打乱顺序

#现在考虑怎么往csv里写入内容
import csv

name = input("what's your name?")
home = input("where's your home?")

with open("exercises/students.csv") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])