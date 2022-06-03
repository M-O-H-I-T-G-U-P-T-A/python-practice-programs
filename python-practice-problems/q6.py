a=int(input("enter lower limit\n"))
b=int(input("enter upper limit\n"))
pr=[]
def sieve(b):
    for i in range (b+1):
        pr.append(1)
    pr[0]=0
    pr[1]=0
    i=2
    while(i*i<=b):
        if(pr[i]==1):
            for j in range(i*i,b+1,i):
                pr[j]=0
        i+=1
sieve(b)
for i in range(a,b+1):
    if(pr[i]==1):
        print(i,end=" ")

