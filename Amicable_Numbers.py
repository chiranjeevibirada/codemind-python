n = int(input())
m = int(input())
x=0
y=0
i=1
for i in range(1,n):
    if n%i==0:
        x+=i
for i in range(1,m):
    if m%i==0:
        y+=i
if x==m and y==n:
    print("Amicable")
else:
    print("Not Amicable")