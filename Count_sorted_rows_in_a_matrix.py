n,m= map(int,input().split())
x=[]
for i in range(n):
    lst=list(map(int,input().split()))
    x.append(lst)
c=0
for i in x:
    if sorted(i)==i or sorted(i, reverse = True) == i:
        c+=1
print(c)