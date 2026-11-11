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

import csv #a mudual
students = []#创建list
with open("exercises/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"],"home": row["home"]})
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

