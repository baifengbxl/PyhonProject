from Person import  Person
from Person import  User
import  pymysql
# 递归：方法自己调用自己   5！=5*4！=5*4*3！
def method(n):
    if n==1:
        return 1
    else:
        return n*method(n-1)
result = method(6)
print(result)

def add(a,b,c):
    print(a,b,c)
    return a+b+c+1
def test():
    add(1,4,8)
    p = Person("tom",12)
    p.eat()
    user = User()
    user.showMessage()

test()
result = add(1,2,3)
print(result)

#主函数，入口
if __name__=="__main__":
  add(1,7,9)