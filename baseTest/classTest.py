__author__ = 'Test-YLL'

# coding:utf-8

class Person:
    def __init__(self,name):
        self.name = name
        self.sex ='男'
    def getName(self):
        return self.name
    def breast(self,n):
        self.breast = n
    def color(self,color):
        print("%s is %s" % (self.name,color))
    def how(self):
        print("%s breast is %s" % (self.name,self.breast))
        print('%s 的好大啊！' % (self.name))


class Girl(Person):
    def setHeight(self):
        print('The height is 170 cm .')
    def how(self):
        print("%s breast is %s" % (self.name,self.breast))
        print('%s 的硕大啊！' % (self.name))

#girl = Person("canglaoshi")
#girl.breast(90)
#girl.color('white')
#girl.how()

class GirlTest:
    pass

class HotGirl(Person,GirlTest):#Python和C++一样，支持多继承的语法。
    '''
    class HotGirl(Person,Girl):
    builtins.TypeError: Cannot create a consistent method resolution
    order (MRO) for bases Person, Girl
    '''
    def __init__(self,name):
        Person.__init__(self,name)
        # super(HotGirl,self).__init__(name)
        self.age=28

    @staticmethod
    def staticTest():
        print("静态方法")

class staticTest:
    @staticmethod
    def staticTest():#后面的括号内没有self
        print("静态方法")
    @classmethod
    def bar(cls):#。类方法的参数也没有self，但是必须有cls这个参数
        print("This is class method bar().")
        print("bar() is part of class:", cls.__name__)

if __name__ =="__main__":
    cang =Girl("canglaoshi")
    cang.setHeight()
    cang.breast(90)
    cang.how()
    #kong = HotGirl("cang")
    #kong.breast(85)
    #kong.how()
    HotGirl("ss").staticTest()
    staticTest.staticTest()
    staticTest.bar()
    # ck = HotGirl('aa')
    # print(ck.age)
    # print(ck.sex)