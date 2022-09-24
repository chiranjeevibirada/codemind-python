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
m = int(input())
s = m+n
next_prime = s + 1
while 1:
    if is_prime(next_prime) == True:
        break
    next_prime += 1
print(next_prime - s)
