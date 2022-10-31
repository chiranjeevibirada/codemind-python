s=input().lower()
s=sorted(s)
x=[]
v=""
for i in s:
    if (i>="a" and i<="z") and s.count(i)==1:
        x.append(i)
        v+=i
print(v)