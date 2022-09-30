n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())
s=0
for i in range(n):
    if x[i]<a or x[i]>b:
        s+=x[i]
print(s)
        