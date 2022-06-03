s=input("Enter a string\n")
c=0
for i in s:
    if(i in "0123456789"):
        c+=int(i)
print(c)
