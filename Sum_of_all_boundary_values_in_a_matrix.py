n,m=map(int,input().split())
x=[]
y=[]
for i in range(n):
    lst=list(map(int,input().split()))
    x.append(lst)
s = 0
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            s += x[i][j]
print(s)