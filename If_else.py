#计算机之所以能做很多自动化的任务，因为它可以自己做条件判断
#比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
#根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
#也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
#根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
#也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')
#注意不要少写了冒号:。
#当然上面的判断是很粗略的，完全可以用elif做更细致的判断：
age = 3
if age >=18:
    print('adult')
elif age >=6:
    print('teenager')
else:
    print('kid')
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻,18.5-25：正常,25-28：过重,28-32：肥胖,高于32：严重肥胖
# -*- coding: utf-8 -*-

height = 1.73
weight = 65
bmi = weight/(height**2)
if bmi<18.5:
    print('您的体重过轻，BMI指数为%.2f' % bmi)
elif bmi>=18.5 and bmi<25:
    print('您的体重正常，BMI指数为%.2f' % bmi)
elif bmi>=25 and bmi<28:
    print('您的体重过重，BMI指数为%.2f' % bmi)
elif bmi>=28 and bmi<32:
    print('您的结果为肥胖，BMI指数为%.2f' % bmi)
else:
    print('您的结果为严重肥胖，BMI指数为%.2f' % bmi)

