x =input("what's x?")
y =input("what's y?")
z= x + y
print(z)
#上述，结果为12，因为x，y被当作string（字符串），所以结果只是字符的链接、拼接。
#可以使用int()函数将字符串转换为整数类型，识别变量为整数，就可以实现运算
z= int(x) + int(y)
print(z)
#上述即为运算方式
'''这好像也是一种注释方式
测试

'''
#测试成功
