names = [
    {"name": "zh", "house": "hubei"},
    {"name": "ljl", "house": "shanxi"},
    {"name": "zsy", "house": "heilongjiang"},
    {"name": "ldq", "house": "shandong"},
]

houses = set()#内置set集合，使用python内置内容可以避免重复造轮子
for name in names:
    houses.add(name["house"])#set里的append写成add

for house in sorted(houses):
    print(house)