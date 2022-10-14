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
s=0
c=0
for i in lst:
        if is_prime(i)==True:
            c+=1
            s+=i
print("{:.2f}".format(s/c))