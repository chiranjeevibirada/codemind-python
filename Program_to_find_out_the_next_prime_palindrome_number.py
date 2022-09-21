def is_prime(n):
    fc = 0
    for i in range(1, n + 1):
        if n%i==0:
            fc +=1
    return fc==2

def is_palindrome(n):
    x = n
    rev = 0
    while n >0:
        r = n%10
        n = n//10
        rev =rev *10+r
    if rev ==x:
        return True
    else:
        return False
n = int(input())
n += 1
while True:
    if is_palindrome(n)==True and is_prime(n)==True:
            print(n)
            break
    n += 1
    
        
        
