n,m = map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
x=[]
y=[]
z=[]
for i in n:
    if i not in m:
        x.append(i)
for i in m:
    if i not in n:
        y.append(i)
for i in x:
    z.append(i)
for i in y:
    z.append(i)
print(*z)