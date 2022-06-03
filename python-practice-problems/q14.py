def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
a=int(input("enter 1st number\n"))
b=int(input("enter 2nd number\n"))
print(gcd(a,b))
