s=input().lower()
x=[]
for i in s:
    if (i>="a" and i<="z") and s.count(i)==1:
        x.append(i)
print(len(x))