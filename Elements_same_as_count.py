n = int(input())
l = list(map(int,input().split()))
x=[]
for i in l:
    if l.count(i)==i:
        if i not in x:
            x.append(i)
if len(x)>0:
    for i in x:
        print(i,end=' ')
else:
    print(-1)
    