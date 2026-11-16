# #python内置的库，会自动处理所有命令行参数的解析工作，即分析命令行参数
# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":#一种规范写法，在命令行里写-n 后面带数字
#     n = int(sys.argv[2])  #如果要设置很多类似于-n的变量，就很麻烦，所以引入新库，argparse  参数解析器
#     for _ in range(n):  
#         print("meow")
# else:
#     print(...)

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to neow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
