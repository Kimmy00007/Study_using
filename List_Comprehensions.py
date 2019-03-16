#列表生成式即list Comprehensions,是Python内置的非常简单却强大的可以用来创建list的生成式.
#举个例子,要生成list[1,2,3,4,5,6,7,8,9,10]可以用list(range(1,11)):
#但如果要生成[1x1,2x2,3x3,...,10x10]怎么做？方法一是循环：
#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list:
#写列表生成式时，把要生成的元素x*x放到前面，后面跟for循环，就可以把list创建出来,十分有用,多写几次,很快就可以熟悉这种语法.
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
#[x*x for x in range(1,11) if x % 2 == 0]
#还可以使用两层循环,可以生成全排列：
#[m + n for m in 'ABC' for n in 'XYZ']
#for 循环其实可以同时使用两个甚至多个变量,比如dict的item()可以同时迭代key和value：
#[k + '=' + v for k,v in d.items()]
#最后把一个list中所有的字符串变成小写：
#[s.lower()for s in L]
#练习
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')