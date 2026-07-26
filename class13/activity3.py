n=int(input("enter the size"))

if n%2==0:
    n=n/2
else:
    n=n//2+1

for i in range(n): 
    num=1
for j in range(n-(i+1)): 
    print("",end="")

for k in range(2*1+1):
    print(num, end="") 
    num+=1
print()

for i in range(n-1,0,-1): 
    num=1

for j in range(n-(i)): 
    print("",end="")

for k in range(1,2*i): # 9 stars
    print(num, end="")
    num+=1
print()