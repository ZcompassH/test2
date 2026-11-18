# name = "张三"
# age = 20
# print(f"我叫{name}，今天{age}岁")

# x = int(input("what's x?"))
# y = int(input("what's y?"))
# print(f"{x + y}, {x - y}, {x*y}, {x/y:.2f}")

# score = int(input("whats score?"))
# if 100 >= score >= 90:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# elif 0 <= score <60:
#     print("E")
# else:
#     print("分数不合法")

# scores = [78, 92, 65, 88, 100, 54]
# #假设
# mx = scores[0]
# mn = scores[0]
# total = 0
# for s in scores:
#     if s > mx:
#         mx = s
#     if s < mn:
#         mn = s
#     total += s
# print("mx:", mx)
# print("mn:", mn)
# print("平均值:", total / len(scores))

# tx = input("say something").lower()
# dic = {}
# for i in tx:
#     if i.isalpha():
#         dic[i] = dic.get(i, 0) + 1
# for i, n in sorted(dic.items(), key=lambda x: x[1], reverse=True):
#     print(i, n)



# def get_even(a):
#     evens = []
#     for i in range(1,a+1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens

# sth = get_even(20)
# print(sth)
# print(f"偶数有{len(sth)}个")


# #Q7:
# path = "sample_text.txt"
# with open(path,encoding="utf-8") as file:
#     lines = file.readlines()
    

# total_lines = len(lines)
# no_empty = 0
# total_chars = 0
# longest = ""

# for i in lines:
#     if i.strip():
#         no_empty += 1
#     total_chars += len(i)
#     if len(i) > len(longest):
#         longest = i

# print("总行数:", total_lines)
# print("非空行数:", no_empty)
# print("总字符数:", total_chars)
# print("最长行:", longest.strip()[:30])

#Q8:
import re
path = "sample_text.txt"
count = {}

with open(path,encoding="utf-8") as f:
    file = f.read().strip()#read是读成一整个字符串，readlines是每行一个元素，readline只读一行

words = re.findall(r"[a-z']+", file.lower())
for w in words:
    count[w] = count.get(w,0) + 1

top10 = sorted(count.items(), key=lambda x: x[1], reverse=True)[:10]
    
for w, n in top10:
    print(f"{w:<12}{n}")
