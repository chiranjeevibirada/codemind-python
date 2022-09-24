def prime(n):
    fc = 0
    for i in range(1, n + 1):
        if n % i == 0:
            fc += 1
    return fc == 2

n = int(input())
found = False
for i in range(1, n + 1):
    if n % i == 0:
        if prime(i) and prime(n//i):
            print(i, n//i)
            found = True
            break
if found == False:
    print(-1)