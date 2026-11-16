def meow(n: int) -> str:#类型提示，如: int   这种，可以用mypy模块来检测代码里的类型是否有错误
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")