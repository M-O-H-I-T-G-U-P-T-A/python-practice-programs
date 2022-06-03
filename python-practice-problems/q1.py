def fun(a,b):
    if (b =="asc"):
        a.sort()
    else:
        a.sort(reverse=True)
    return a

a=eval(input("Enter a list of numbers\n"))
b=input("enter string\n")
p=fun(a,b)
print(p)

