n = int(input())
x = list(map(int,input().split()))
l=[]
for i in range(n):
    if x[i] not in l:
        l.append(x[i])
print(*l)