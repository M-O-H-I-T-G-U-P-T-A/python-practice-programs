def calc(a,b,c):
    if(b=="+"):
        return a+c
    if(b=="-"):
        return a-c
    if(b=="*"):
        return a*c
    if(b=="/"):
        return float(a)/c
a=int(input("Enter a\n"))
b=input("Enter b\n")
c=int(input("Enter c\n"))
print(calc(a,b,c))
