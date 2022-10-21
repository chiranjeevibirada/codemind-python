n,m=map(int,input().split())
x=[]
for i in range(n):
    lst=list(map(int,input().split()))
    x.append(sum(lst))
print(*x)