def digit(n):
    s=0
    while n:
        s+=n%10
        n=n//10
    return s

n = int(input())
lst = list(map(int,input().split()))
a=0
for i in lst:
    a+=digit(i)
print(a)