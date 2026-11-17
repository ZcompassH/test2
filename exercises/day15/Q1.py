name = "张三"
age = 20
print(f"我叫{name}，今天{age}岁")

x = int(input("what's x?"))
y = int(input("what's y?"))
print(f"{x + y}, {x - y}, {x*y}, {x/y:.2f}")

score = int(input("whats score?"))
if 100 >= score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 0 <= score <60:
    print("E")
else:
    print("分数不合法")

scores = [78, 92, 65, 88, 100, 54]
#假设
mx = scores[0]
mn = scores[0]
total = 0
for s in scores:
    if s > mx:
        mx = s
    if s < mn:
        mn = s
    total += s
print("mx:", mx)
print("mn:", mn)
print("平均值:", total / len(scores))