#库/package   一个库有很多模块，模块是一整个.py文件，这些模块会有别人写好的函数供你调用。

def main():
# import random      #引入random库

# coin = random.choice(["heads","tails"])
# print(coin)

# number = random.randint(1,10)#在一个数字范围里随机等概率生成
# print(number)

# cards = ["jack","queen","king"]
# random.shuffle(cards)
# print(cards)   #这样打印的是cards的这个列表，并重新排序
# for card in cards:
#     print(card)   

# import statistics#译为统计学

# print(statistics.mean([100,90,94]))  #mean,取平均值


import sys # system的缩写，这个模块可以让你能够使用命令行参数，实现高效互动

print("hello,my name is",sys.argv[1]) #sys.argv[]里面已经存了索引为0的内容，为这个程序的名字

if len(sys.argv) < 2:
    sys.exit("few arguments")   # exit可以打印后面的内容并直接退出程序，这样可以将print写在最后，且不在if语句里
elif len(sys.argv)>2:    #这里只需要了解exit的用法即可
    sys.exit("too mant arguments")

print("hello,my name is",sys.argv[1])

#  sys.argv 可以打印多个量，
for arg in sys.argv：
    print("hello,my name is",arg)#但是你会多打印一个量，就是索引为0的程序名字，
#因此，这里引入切片语法，[1:]  ,这样表示从索引1到一个用户给的值，可以避开0，或者你想要其他的范围

#你可以用pip模块来快速下载包，只需要知道包名，pip是py自带的库
#比如，直接在终端输入：pip install cowsay，就可以下载名为cowsay这个包/package
#然后就可以引用  import cowsay

#request这个包，可以直接在终端访问以HTTP、HTTPS开头的URL资源
#用request.get(网址)
#print(respond.jspn())   这里的respond只是自己随便定的一个变量，但它可以和json联动

#JSON是一种文本类型，用request访问，可以用JSON来展现内容

#最后，你可以创建自己的package，但在最后调用主函数时，应该加入
if __name__ == "__main__"
    main
#意思是，如果调用这个库时，程序名不为库的名字，不运行主函数，这样调用这个包的用户就不会莫名其妙run
#算是给main函数加了一道身份确认，但这个package里的其他函数，别人就可以无打扰的调用了