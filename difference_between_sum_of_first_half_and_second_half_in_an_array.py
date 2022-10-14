n = int(input())
lst=list(map(int,input().split()))
s=lst[0:n//2:]
p=lst[n//2:n:]
x=0
y=0
for i in s:
    x+=i
for i in p:
    y+=i
if x>y:
    print(x-y)
else:
    print(y-x)