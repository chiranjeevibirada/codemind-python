n=int(input())
li=list(map(int,input().split()))
a,b=map(int,input().split())
li.sort()
#print(li)
#print(a,b)
if a in li:
    a=li.index(a)
else:
    a=0
if b in li:
    b=li.index(b)
else:
    b=n
w=0
for i in range(a,b):
    w=li[i]
    break
if w==0:
    print(-1)
else:
    print(w)
    



