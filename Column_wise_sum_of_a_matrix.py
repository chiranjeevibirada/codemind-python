n,m=map(int,input().split())
x=[]
for i in range(n):
    lst=list(map(int,input().split()))
    x.append(lst)
for i in range(m):
    s = 0
    for j in range(n):
        s+=x[j][i]
    print(s, end = ' ')