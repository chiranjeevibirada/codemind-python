n = int(input())
x = list(map(int,input().split()))
c=0
for i in range(n):
    if x[i]==0 or x[i]==1:
        c+=1
if n==c:
    print("True")
else:
    print("False")
        