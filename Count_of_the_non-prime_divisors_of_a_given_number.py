def is_prime(x):
    fc=0
    for i in range(1,x+1):
        if x%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False

n = int(input())
fc=0
for i in range(1,n+1):
    if n%i==0:
        if is_prime(i)==False:
            fc+=1
print(fc)
    