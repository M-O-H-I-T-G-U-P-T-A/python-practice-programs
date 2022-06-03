a=eval(input("enter a list\n"))
d={}
for i in a:
    d[i]=0
for i in a:
    d[i]=d[i]+1
max=-1
maxe=None
for i in d:
    if(d[i]>max):
        max =d[i]
        maxe=i
print(maxe)
