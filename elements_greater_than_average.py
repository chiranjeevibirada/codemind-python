n = int(input())
x = list(map(int,input().split()))
avg=0
s=0
cnt=0
for i in x:
    s+=i
    avg = s//n
for i in range(n):
    if x[i]>=avg:
        cnt+=1
print(cnt)