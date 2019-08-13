'''
*
**
***
****
'''
i =0
while i<4:
  j=0
  while j<=i:
    print("*",end=" ")
    j = j + 1

  print()
  i=i+1


for i in  range(4):
    for j in range(i+1):
        print("*",end="\t")
    print()

#continue: 跳过本次循环(继续执行)  break：跳出当前所在循环(终止)

for i in  range(10):
    if i==5:
        break;
    print("i:",i)
'''
1.先从控制台输入年和月
2.算出输入的年份到1900年多少天  366或者365
3.算出当年的1月距离输入的月份有多少天  月份计算(28,29,30,31)
4.打印  
'''

