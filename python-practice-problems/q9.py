s=input("Enter a string\n")
for i in "abcdefghijklmnopqrstuvvwxyz":
    for j in s:
        if(i==j):
            print(i,end='')
        if(i.capitalize()==j):
            print(i.capitalize(),end="")

