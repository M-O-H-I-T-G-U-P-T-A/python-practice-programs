a=eval(input("enter list of directions"))
dict={"NORTH":0,"SOUTH":0,"EAST":0,"WEST":0}
for i in a:
    dict[i]+=1
y=0
x=0
y=dict["NORTH"]-dict["SOUTH"]
x=dict["EAST"]-dict["WEST"]
d=[]
if(y<0):
    d.append("SOUTH")
    y=-y
elif(y>0):
    d.append("NORTH")
d=d*y
d1=[]
if(x<0):
    d.append("WEST")
    x=-x
elif(x>0):
    d.append("EAST")
d1=d1*x
d=d+d1
print(d)
    
