def prime(x):
    fc=0
    for i in range(1,x+1):
        if x%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
    
n = int(input())
s =n
rev=0
while n>0:
    r = n%10
    rev = rev*10+r
    n = n//10
if prime(s)==True and prime(rev)==True:
    print("circular prime")
elif prime(s)==True or prime(rev)==True:
    print("prime but not a circular prime")
else:
    print("not prime")