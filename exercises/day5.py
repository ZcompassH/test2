#morning!

#循环

# i = 0
# while i  < 3 :
#     print("hello")
#     i  +=  1         #表示递增的python写法,  or   i = i + 1

#for循环
#for i in [0,1,2] :       #[]是一个list
# for i in range (3) :        #range定义一个范围，可以理解为从0开始，逐渐 + 1 ，知道你定义的数为止，range至少给一个参数
#     print   ("hello")

# #这里i只作为一个参数来表述某数在循环，并没有真正调用它，python里遇到这种调用，可以用_表述一个参数
# for _ in range (3):
#     print ("hello")

#python 写法
print ("hello" * 3 )  #发现，hello不会自己换行
print ("hello\n" *3)    #但是这样print完之后会出现一行空输出，不美观
print ("hello\n" *3,end="")  #因为print默认结尾是\n，加入end=“”，即末尾什么都没有，取消了默认

while True:  #无限循环，可以定义打破规则
    n = int(input("what's n ?"))
    if n < 0 :
        continue  #继续循环
    if n > 0 :
        break   #break即为打破循环,,,当然这里可以不用continue，可以直接定义什么时候打破循环即可

for _ in range (n):
    print ("hello" )