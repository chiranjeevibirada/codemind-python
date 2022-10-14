n,m = map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
x = []
y = []
z = []
for i in n:
    if i not in x:
        x.append(i)
for i in m:
    if i not in y:
        y.append(i)
for i in x:
    if i in y:
        z.append(i)
print(*z)