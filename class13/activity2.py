n=int(input("enter the size of flyoids triangle"))
num=1
for i in range(n):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()