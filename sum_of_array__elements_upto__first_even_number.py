n = int(input())
lst=list(map(int,input().split()))
x=0
for i in lst:
    if i%2==1:
        x+=i
    else:
        break
print(x)