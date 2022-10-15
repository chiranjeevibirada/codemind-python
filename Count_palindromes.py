def pal(n):
    s=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==s:
        return True
    return False
n = int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if pal(i)==True:
        c+=1
print(c)