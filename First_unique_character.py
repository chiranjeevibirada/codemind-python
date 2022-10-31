s=input().lower()
x=[]
c=0
for i in s:
    if (i>="a" and i<="z") and s.count(i)==1:
        x.append(i)
        c+=1
        print(*x)
        break
if c==0:
    print(-1)