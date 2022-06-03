def fun(a):
    l=len(a)
    s="*"*(l-4)
    s=s+a[l-4::]
    return s
a=input("Enter credit card number\n")
print(fun(a))
