s=input().lower()
x=[]
for i in s:
    if (i>="a" and i<="z")  and i not in x:
        x.append(i)
print(len(x))