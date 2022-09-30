n = int(input())
x = list(map(int,input().split()))
cnt=0
for i in range(1,n-1):
    if x[i]%2==1 and x[i-1]%2==0 and x[i+1]%2==0:
        cnt+=1
print(cnt)