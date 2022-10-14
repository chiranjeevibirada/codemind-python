n = int(input())
lst=list(map(int,input().split()))
k = int(input())
x=0
for i in lst:
    if i<=k:
        x+=i
    else:
        break
print(x)