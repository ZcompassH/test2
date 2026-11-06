#morining!

#条件语句

# x =int(input("what's x?"))
# y =int(input("what's y?"))
# if x < y:
#     print(x ,"is less than" ,y)
# if x > y:
#     print(x ,"is greater than" ,y)
# if x == y:
#     print(x ,"is equal to" ,y)
# #这样写会本质是三次独立的判断，效率最低，可以使用elif语句，elif是else if的缩写，
# # 表示如果前面的条件不成立，就判断后面的条件
# if x < y:
#     print(x ,"is less than" ,y)
# elif x > y:
#     print(x ,"is greater than" ,y)
# elif x == y:
#     print(x ,"is equal to" ,y)
# #这样写只要命中就会直接跳到最后的stop，但如果x，y相等，就会先判断x < y不成立，再判断x > y不成立，最后判断x == y成立，所以效率还是不高
# #可以使用else语句，else表示如果前面的条件都不成立，就执行else
# if x < y:
#     print(x ,"is less than" ,y)
# elif x > y:
#     print(x ,"is greater than" ,y)
# else:
#     print(x ,"is equal to" ,y)
# #这样逻辑最清晰，效率最高，且代码最简洁


# #如果只想验证x是否等于y，可以使用or
# if x < y or x > y:                    #这里直接使用!=来表示不等于更简洁
#     print(x ,"is not equal to" ,y)
# else:
#     print(x,"is equal to",y)


# score =int(input("score: "))
# if score >= 90 and score <= 100:
#     print("grade: A")
# elif score >= 80 and score < 90:
#     print("grade: B")
# elif score >= 70 and score < 80:
#     print("grade: C")
# else:
#     print("grade: D")
# #python中可以使用and和or来连接多个条件，and表示两个条件都成立，or表示两个条件有一个成立就可以
# #但也有范围的表示方式
# if 90 <= score <= 100:
#     print("grade: A")
# elif 80 <= score < 90:
#     print("grade: B")#sth like this
# #但其实在这种情况，elif score >= 80:就可以了，因为前面已经判断过score < 90了，
# # 所以这里不用再判断score < 90了
# #elif也遵循上到下，所以上面的如果成立，为ture，那么会直接跳入stop，流程逻辑图似乎更好解释
# if score >= 90:
#     print("grade: A")
# elif score >= 80:
#     print("grade: B")
# elif score >= 70:
#     print("grade: C")    #sth like this
# else:
#     print("grade: D")


#boolean类型，布尔类型，只有两个值，True和False，首字母大写
#   %作用是取模，即得到某数的余数

def main():
    x = int(input("what's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return  True if n % 2 ==0  else False   #甚至直接写成return n % 2== 0
    return  n % 2 == 0

main()

#最后介绍一个match
                # case“ ”：
                # case“ ”：
                # case_ :   (兜底，default)
                #可以做到类似if   elif  else  ，还有更多作用...