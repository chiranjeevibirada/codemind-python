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
c=0
b = max(lst)
a = min(lst)
a=lst.index(a)
b=lst.index(b)
if a > b:
    a, b = b, a
for i in range(a,b+1):
        if is_prime(lst[i])==True:
            c+=1
print(c)