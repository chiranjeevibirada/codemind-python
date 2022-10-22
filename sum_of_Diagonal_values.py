n,m = map(int,input().split())
x = []
for i in range(n):
    lst = list(map(int,input().split()))
    x.append(lst)
s=0
for i in range(n):
    for j in range(m):
        if i==j or i+j==n-1 or j==i or j+i==m-1:
            s+=x[i][j]
print(s)