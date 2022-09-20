def is_prime(n):
    fc =0
    for i in range(1,n+1):
        if n%i==0:
            fc +=1
    if fc==2:
        return True
    return False
N = int(input())
k=N
s=0
c=0
z=0
while N:
    r = N%10
    s = r
    c+=1
    N = N//10
    if is_prime(s):
            z+=1
    else:
            continue
if z==c and is_prime(k):
    print("Mega Prime")
else:
    print("Not Mega Prime")