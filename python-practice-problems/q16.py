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
sieve(1000000)
print("Enter 0 to quit\n")
n=int(input("Enter n\n"))
while(n!=0):
    for i in range(1,n+1):
        if(pr[i]==1):
            print(i,end=" ")
    print("\nEnter 0 to quit\n")
    n=int(input("Enter n\n"))
