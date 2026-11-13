# 正则表达式  regex

import re #这个库可以表达很多模式，里面的search(par,str,falgs=0)

#写一个检查用户输入是否符合邮箱要求的函数
email = input("what's your email?").strip() #.strip消除输入内容首尾的空格，避免用户误输入

if re.search(r"^.+@.+\.edu$",email):#正则表达式，r表示是常规字符，这样才能使用转义字符\,
    print("Valid")      #^表示开头，.表示一个字符，+表示左边内容出现一次或多次，$表示结尾（除neline）
else:
    print("Invalid")
#notes：  *表示左边内容出现0次或多次，[]表示只允许括号内的字符出现，[^]表示不允许括号里的内容出现，与"."都是表示字符内容
#表达式内，{1}也可以表示一个字符，但繁琐，不如用.     []内可以用-来表示范围，如[a-zA-Z0-9_]
#而[a-zA-Z0-9_]可以直接表示为\w   因为这个范围很常见，已经内置到re里了  \W表示否定这个范围
#d表示0-9，\D表示反例    \s表示空白字符，如空格和tab产生的空白字符，反之\S

if re.search(r"^\w+@\w+\.edu$",email)#现在可以写成这样
if re.search(r"^\w+@\w+\.edu$",email,re.IGNORECASE) #加入falgs，re.IGNORECASE可以忽略大小写z
# A|B  either A or B      (...) a group    (?:...) non-capturing version
if re.search(r"^\w+@(\w\.)?\w+\.edu$",email,re.IGNORECASE)  #这样可以访问带子域名的地址或不带，把？换成*可以带更多
#当然，已经有人写好了关于邮箱输入的正则表达式，只需找相关需要的库即可



name = input("what's your name?").strip()
#正则表达式里，()不仅表达group，还可以用来捕获，里面的内容会被capture并给予返回值
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    #last, first = matches.groups()
#上述一行可以写成：
    #last = matches.groups(1)
    #first = matches.groups(2)

    #name = f"{first} {last}"
#其实if以下的都可以简化成：
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

#海象运算符 :=  能做到将右侧赋值到左侧的同时进行布尔判断，就可以省略掉刚刚赋值后就要判断的场景
#如上述的matches，可以直接写成：
if matches := re.search(r"^(.+), *(.+)$", name):

url = input(ULR: ).strip()
    #sub即substitute代替，re.sub(pattern, repl, string, cpount=0, falgs=0)
username = re.sub(r"^(https?://)?(www\.)?wtitter\.com/", "", url)
print(f"Username: {username}")
#但其实这里sub并没有search好用，切search：
if mat := re.search(r"^(https?://)?(www\.)?wtitter\.com/(.+)$"):
    print(f"Username:", mat.group(1))#这里会导致捕获www.   改成group(2)才行
#除非用非捕获符号(?:),引号后面的内容不会被捕获，即(?:www\.)?，这样这部分不会被捕获，就可以写group(1)

#介绍：
#re.split(pattern, string, maxsplit=0, flags=0)
#re.findall(pattern, string, falgs=0)  在字符串的不同位置搜索多个相同模式，处理多个匹配结果？