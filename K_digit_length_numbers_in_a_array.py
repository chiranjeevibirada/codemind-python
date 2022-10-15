n,k = map(int,input().split())
lst= list(map(int,input().split()))
c=0
for i in lst:
    if k==len(str(abs(i))):
        c+=1
print(c)