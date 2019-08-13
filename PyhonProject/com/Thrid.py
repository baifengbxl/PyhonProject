# 分支语句  if  if... else..   if..elif ..elif ..else
'''
  格式:
    if  表达式:
       代码段
       >  >=  <  <= == in包含
'''
score = 88
list=[90,98,76,88]
# if score in list:
#     print("优秀")
if score>=90:
    print("优秀")
elif score>=80 and score<90:
    print("良好")
elif score>=60 and score<80:
    print("及格")
else:
    print("不及格")
print("over")

