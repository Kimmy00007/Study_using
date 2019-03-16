class Student(object):
    pass
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
#表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，
#这是所有类最终都会继承的类。
#定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
bart= Student
bart



bart.name = 'Bart Simpson'
bart.name
'Bart Simpson'
class Student(object):


    def __init__(self,name,score):
        self.name = name
        self.score = score
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
#######数据封装########
#面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和Score这些数据，我们可以通过函数来访问这些数据，
#比如打印一个学生的成绩：
def print_score(std):
    print('%s:%s' % (std.name,std.score))
    print_score(bart)

#但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把
#"数据"给封装起来了，这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))
#要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法。只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：

#这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被
#“”“”“”“”“”“”“”“”“”“”“”“”“”“"封装"起来了，调用很容易，单却不用知道内部实现的细节。封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
class Student(object):



    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
