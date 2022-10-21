n,m=map(int,input().split())
x=[]
y=[]
for i in range(n):
    lst=list(map(int,input().split()))
    x.append(lst)
for i in range(m):
    z = []
    for j in range(n):
        z.append(x[j][i])
    y.append(z)
c=0
for i in y:
    if sorted(i)==i or sorted(i, reverse=True)==i:
        c+=1
print(c)