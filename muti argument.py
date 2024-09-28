# list1=list(map(int,input("Enter").split()))
# print(list1)
#
# dict1={}
# num=int(input("enter : "))
# for i in range(num):
#     key=input(" enter: ")
#     value=input("Enter : ")
#     dict1[key]=value
# print(dict1)

def myfun(*args):
    a=0
    for i in args:
        a+=i
    return a
print(myfun(1,2,3,4))

def myfun(**kwargs):
    return kwargs

print(myfun(a="name",b="lastnam",c="address"))