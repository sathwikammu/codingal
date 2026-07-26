print("pick your holiday type")
x=input("beach holiday as 1 and mountain holiday as 2")
if x=="1":
    y=("swimming as 1 and relaxing as 2")
    if y=="1":
        print("swimming is good in mrngs")
        print("carry sunscreen")
    else:
        print("relaxing near beach will reduce stress")
        print("carry snacks and water bottle")

elif x=="2":
   z=input("hiking as 1 and exploring as 2") 
   if z=="1":
       print("carry watwr bottles")
       print("wear comfortable clothes")
   else:
       print("carry camera")
       print("capture good snaps")
else:
    print("invalid input")