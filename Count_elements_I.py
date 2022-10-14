n,m = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
a=list(a)
b=list(b)
x=[]
c=0
w=0
if m<=n:
    for i in b:
        if i in a:
            x.append(i)
else:
    for i in a:
        if i in b:
            x.append(i)
print(len(x))
