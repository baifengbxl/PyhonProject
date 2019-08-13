
def write():
    f =open("E:/test.txt","w")
    f.write("abcdefg")

def read():
    f = open("E:/test.txt","r")
    result = f.read()
    print(result)
# write()
read()