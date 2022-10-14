def is_prime(x):
    fc=0
    for i in range(1,x+1):
        if x%i==0:
            fc+=1
    if fc==2:
        return True
    return False
n = int(input())
lst=list(map(int,input().split()))
k = int(input())
c=0
for i in lst:
    if i<=k:
        if is_prime(i)==True:
            c+=1
print(c)