def is_prime(n):
    fc =0
    for i in range(1,n+1):
        if n%i==0:
            fc +=1
    return fc==2
    
t = int(input())
for i in range(t):
    n = int(input())
    prev_prime = n
    while 1:
        if is_prime(prev_prime) == True:
            break
        prev_prime -= 1
            
    next_prime = n
    while 1:
        if is_prime(next_prime) == True:
            break
        next_prime += 1
    if n - prev_prime <= next_prime - n:
        print(prev_prime)
    else:
        print(next_prime)