num=int(input("enter: "))
for i in range(2,num):
    if i>1:
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            print(i)