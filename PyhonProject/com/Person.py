'''
面向对象    对象：有 特征（属性） 和 功能（函数，方法）组成 ，实实在在存在的实体
            类：是相同对象特征和功能的集合,是抽象的，模板
        属性定义： 1.在类中直接定义（变量）
                  2.在__init__方法中定义,初始化
        函数定义:
           格式：def  方法名(self,[参数1,参数2...]):
           返回结果:  1.不返回   2.通过return进行返回
        对象的创建:  对象名  = 类名()
        属性的调用： 对象名.属性名
        方法的调用： 对象名.方法名()
'''
class Person:
    # name=None
    # age=0
    # 构造函数，构造器
    def __init__(self,n,a):#形参
        self.name=n
        self.age=a
    def eat(self):

        print("eat...")
    def add(self,num1,num2):
        return num1+num2
    def method(self,n1,*args):
        print(n1,args)
    def method2(self,n1,**a):
        print(a)

    @staticmethod
    def sum(a,b):
        print(a,b)

class User:
    def showMessage(self):
        print("user message...")
#
# Person.sum(1,2)
# '''
# 对象创建 : 对象名=类名()
# '''
# p1 =Person("孬蛋",0)
# p1.name = "哪吒"
# p1.name="孙悟空"
# # p1.age=3
# print(p1.name)
# print(p1.age)
# p1.eat()
# result = p1.add(123,789)
# print(result)
# p1.method(1,34,56,78)
# p1.method2(1,name="xiaoming",age=18)
# p1.sum(3,0)