n = int(input())
lst=list(map(int,input().split()))
c=0
d=0
for i in range(2,n):
    if lst[i]==lst[i-1]+lst[i-2]:
            c+=1
    else:
        d = 1
        break
if c>0 and d==0:
    print('yes')
else:
    print('no')