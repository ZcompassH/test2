#假设zh是一个list，那么*zh就可以解包这个list，如果是字典，**zh就可以解包这个字典
#但是list和dict的参数是确定的，一开始就设置好的
def zh(*args, **kwargs):#args和kwargs是默认写法，可以改。这种写法是给函数一个可变数量的参数，
                                 #args叫位置参数，kwargs叫命名参数
    print("Positional:", args)#args像list  ，而kwargs像dict

zh(100,50,25,5,1)#现在可以随意输入传入的参数数量，所以说是可变数量的参数