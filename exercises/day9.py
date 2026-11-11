#morning

#file I/O


#在之前的函数中，只是一些简单的一次性互动，需要用户每次输入参数值来运行，
# 且每次都会重置，无法记录、保存我们输入，计算后的结果
# name = input("what's your name?")
# print(f"hello",name)

#介绍open函数
#open():   #它可以打开或创建文件，并对文件进行编辑输入输出

# name = input("waht's your name?")

# file = open("names.txt","w") #译为，打开（没有就创建）names.txt这个文件，“w“为write缩写，即可以编写
# file.write(name)    #译为，将name写入文件
# file.close()       #关闭文件
# #上述写法会有问题，"w"会导致每次重新运行时，会覆盖文件之前保存的内容。每次打开都会重新创建并写入

# #解决方式只要把"w"改成"a"即可，a即append，译为追加，会在文件末尾追加这次的输入
# file = open("names.txt","a") 
# # file.write(name)    #但这样会导致每次输入的内容首尾相连，因此需要换行
# file.write(f"{name}\n")  #这样就可以每次输入是单独一行了，当然，方法多样
# file.close()

#with语句，为避免程序员忘记写close函数来关闭文件，造成文件损坏或丢失
#with  open(...)  as  变量名，这是with语句的固定搭配
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")#效果如此，在写入之后，或open结束后，会自动关闭文件

#已经用上述语句写入了三个名字，现在介绍"r"即read，读取模式
# with open("names.txt","r") as file: 
#     lines = file.readlines() #readlines函数就可以读取文件中的每一行数据

# for line in lines:
#     print("hello,",line.rstrip())#rstrip()函数可以去除每一行末尾的换行符，
#     #不然这里print再创建一个换行符就会两次换行，或者用end=    去除print的\n也可以

# #简洁写法
# with open("names.txt","r") as file:
#     for line in file:
#         print("hello,",line.rstrip())
#怎么实现每次读取打印，可以自动按字母顺序来排序呢？
names = [] #创建list

with open("names.txt")as file: #open默认是r模式，用r模式可以不写
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):#sorted是排序函数，按字母排序
    print(f"hello,{name}")