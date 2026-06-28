#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?

bp=input("enter the number") #bp is buing price
sp=input("enter the number") #sp is selling price
bp=int(bp)
sp=int(sp)



if bp>sp:
    print("he has loss")
else:
    print("he has profit")
