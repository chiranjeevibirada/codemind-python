n = int(input())
l = list(map(int,input().split()))
c=0
x=[]
for i in l:
    if l.count(i)>0:
        if i not in x:
            x.append(i)
for i in x:
    print(i,l.count(i),end = ' ')