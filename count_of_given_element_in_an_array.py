n = int(input())
x = list(map(int,input().split()))
z = int(input())
cnt=0
for i in x:
    if z == i:
        cnt+=1
print(cnt)

    