s=input().lower()
x=[]
z=[]
#y=sorted(s)
for i in s:
    if (i>="a" and i<="z") and i not in x:
        x.append(i)
x=sorted(x)
print("".join(x))