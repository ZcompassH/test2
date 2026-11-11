import csv #a mudual
from pathlib import Path#可以让文件永远指向自己的位置，从而解决open的问题
students = []#创建list
with open("exercises/students.csv") as file:#这里始终运行失败，test.py在exercises里,和students.csv同级，
    reader = csv.reader(file)
    for name,home in reader:
        students.append({"name": name,"home":home})
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")