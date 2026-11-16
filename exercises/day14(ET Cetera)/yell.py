def main():
    yell("this", "is", "cs50")

def yell(*words):
    uppercased = map(str.upper, words)#map函数可以传入某个函数的内容并调用它，对一些参数进行操作，这样可以省去写循环函数的时间
    print(*uppercased)

if __name__ == "__main__":
    main()

#list comprehensions 列表推导式
uppercased = [word.upper() for word in words] #用这个替换map效果也是一样的，也可以做到省去写循环函数，效率高
#filter函数，传入一个函数用来做判断，再传入一个数据，用来判断True or False，过滤数据
#列表推导式后面也可以加入if来过滤，这两种方法作用相似
#也存在字典推导式，写法类似list comprehension

#generator  这个库里面有一个yield，可以替换return。
# 作用是每次只返回一个值，return是一次返回所有值，当循环次数太多，数据太大的时候会导致电脑内存不够而卡死，yield很好的解决了这个问题
#yield的特性返回的东西，技术上称作iterator迭代器