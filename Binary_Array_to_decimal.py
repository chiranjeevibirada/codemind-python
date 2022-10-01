n = int(input())
x = list(map(int,input().split()))
s=0
y=0
for i in range(n-1,-1,-1):
    s+=x[i]*(2**y)
    y+=1
print(s)