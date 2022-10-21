n,m=map(int,input().split())
x=[]
y=[]
for i in range(n):
    lst=list(map(int,input().split()))
    x.append(sum(lst))
print(max(x))
for i in range(n):
    lst=list(map(int,input().split()))
    x.append(lst)
for i in range(m):
    s=0
    for j in range(n):
        s+=x[j][i]
        y.append(s)
print(max(y))
if max(y)>max(x):
    print(max(y))
else:
    print(max(x))