print("Hello, World!")
name=input("what's your name? ")
print("Hello", name)
print(f"Hello, {name}")
print("Hello " + name)
print("Hello," ,name)

#day3 补充
name=name.capitalize()#.capitalize()函数将字符串的首字母大写，其他字母小写
print(f"Hello, {name}")
name=name.upper()#.upper()函数将字符串的所有字母大写
print(f"Hello, {name}")
name=name.lower()#.lower()函数将字符串的所有字母小写
name=name.title()#.title()函数将字符串的每个单词的首字母大写
print(f"Hello, {name}")
#所以英文名似乎用title更合理
#且函数可以串联，或者说链式调用，如下：
name=name.lower().title()#这样无论怎么输入，都可以将首字母大写，其他小写