'''
1.先从控制台输入年和月
2.算出输入的年份到1900年多少天  366或者365
3.算出当年的1月距离输入的月份有多少天  月份计算(28,29,30,31)
4.打印
'''

year= input("请输入你的年份: ")
year=int (year)
print(year)

month=input("请输入你的月份: ")
month=int (month)
print(month)

year_value=(year-1900)*365
print(year_value)

month_value=(month-1)*30
print(month_value)

