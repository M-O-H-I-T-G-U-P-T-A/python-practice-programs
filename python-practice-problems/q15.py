s=input("Enter a string\n")
a=0
d=0
sc=0
for i in s:
    if(i.isdigit()):
        d+=1
    elif(i.isalpha()):
        a+=1
    else:
        sc+=1
print("alphabets=",a)
print("digits=",d)
print("special characters=",sc)
