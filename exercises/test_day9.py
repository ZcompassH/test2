# import csv #a mudual
# from pathlib import Path#可以让文件永远指向自己的位置，从而解决open的问题
# students = []#创建list
# with open("exercises/students.csv") as file:#这里始终运行失败，test.py在exercises里,和students.csv同级，
#     reader = csv.reader(file)
#     for name,home in reader:
#         students.append({"name": name,"home":home})
# for student in sorted(students,key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


    #最终理解：你现在在看test_day9.py,但现在终端位置并不在这里，而在你打开的文件夹，左侧树状的第一层，test2

# import csv #a mudual
# students = []#创建list
# with open("exercises/students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"],"home": row["home"]})
# for student in sorted(students,key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

import csv

name = input("what's your name?")
home = input("where's your home?")

with open("exercises/students.csv", "a",newline="") as file: #windows系统，如果 csvfile 是文件对象，必须用 newline='' 打开。这是py官方的原话
    writer = csv.writer(file)
    writer.writerow([name,home])
#          输入：一个列表（每个元素是一个字段） 输出：文件里的一行文本 + 行尾符(/r/n)即换行，但windows会再翻译，导致换两行


#open还可以打开音频、图片等类型，可以用图片制作gif
import sys  #命令行参数模块

from PIL import Image

images = []

for arg in sys.argv[1:]: #切片，从索引1往后取，避免第一个文件，即文件名称
    image = Image.open(arg)
    images.append(image)
#第一帧images[0]
images[0].save(    #这里只添加一张图，可以用切片来添加多个图片/帧  #停留200ms，    无限循环
    "costumes.gif",save_all=True, append_images=[images[1]],duration=200, loop=0
)
#为什么用 images[0].save() 而不是别的？
#因为 Pillow 的规矩是："用第一张图当画布，然后把其他帧挂上去"。第一张是主体，剩下的通过 append_images 附上。