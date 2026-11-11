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
#上述写法会有问题，"w"会导致每次重新运行时，会覆盖文件之前保存的内容。每次打开都会重新创建并写入