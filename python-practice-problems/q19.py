import random
n=random.randint(1000,9999)
n=str(n)
print("you have 10 chances to guess\n")
n1=sorted(n)
for i in range(10):
    print("enter ",i+1," choice :",end="")
    p=input()
    p1=sorted(p)
    if(p==n):
        print("R")
        break
    elif(n1==p1):
        print("Y")
    else:
        print("B")
