#今天学单元测试，即测试自己的代码。

#pytest是一个库，用git install pytest下载，它可以快速测试代码是否有误

import pytest_

#比如我有一个hello函数，现在需要测试是否有bug

def test_hello():
    assert hello(zh) == "hello,zh"
#assert意为“断言”，这个语句意思是断言hello函数，参数为zh时结果一定为hello，zh，如果不是就会报错

#可以有很多方式测试自己的代码，但学习课程里是另外创建一个py文件，即测试文件。
#方法大多都是举例测试，看是否通过，只不过有很多写法，效率不同。