# 元组  ()--->查询 下标从0开始
tup = ("xiaoming","tom","jack")
print(tup[0])
print(tup[1])
print(tup[2])
#print(tup[3])
print(len(tup))

#列表 [] 进行增加，删除，更新，查询

list=[345,987,670,456,9,12,56,76]
# 查询
print(list[0])
print(list[1:4])
print(list[2:])
print(list[0:7:2])
print(list[7:0:-1])
# 添加数据,在尾部追加
list.append(998)
print(list)
# 指定位置添加元素
list.insert(1,700)
print(list)
list+=[999]
print(list)
# 更新
list[3]=123
print(list)
# 删除
list.remove(345)
print(list)
list.pop(0)
print(list)

# 字典   {键:值,键:值}
dict={"name":"小明","age":18,"sex":"男"}
# 通过key获取value
uname = dict["name"]
print(uname)
uage = dict["age"]
print(uage)
usex=dict["sex"]
print(usex)
dict["tel"]="18912011066"
print(dict)
dict["age"]=99
print(dict)




