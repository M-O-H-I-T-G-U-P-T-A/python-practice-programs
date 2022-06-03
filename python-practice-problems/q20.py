pr=[]
cpr=[]
pri=[]
for i in range(1000000+1):
    cpr.append(0)


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


for i in range(1000000+1):
    if(pr[i]==1):
        pri.append(i)


def rotate(a):
    a=str(a)
    b=a[1::]
    b+=a[0]
    b=int(b)
    return b


def isodd(a):
    a=str(a)
    for i in a:
        if(i in "02468"):
            return 0
    return 1


def nd(a):
    a=str(a)
    return len(a)


cpr[2]=1


for i in pri:
    if(isodd(i) and  cpr[i]==0):
        l=nd(i)
        p=i
        c=0
        for j in range(l):
            p=rotate(p)
            if(pr[p]==1):
                c+=1
        if(c==l):
            for j in range(l):
                p=rotate(p)
                cpr[p]=1

                
c=0
for i in range(1000000+1):
    if(cpr[i]==1):
        c+=1
        print(i,end =" ")
print("\nthe number of circular primes are ",c)

    

