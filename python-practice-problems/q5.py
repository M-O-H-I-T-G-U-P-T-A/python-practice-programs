def find(a):
    b=[]
    for i in range(102):
        b.append(0)
    for i in a:
        b[i]+=1
    for i in range(len(b)):
        if(b[i]>=2):
            return i
a=eval(input("Enter a list of numbers"))
print(find(a))
