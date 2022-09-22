n = int(input())
f,s = 0,1
ne = f*s
c=0
while ne<=n:
    if ne==n:
        print("YES")
        c=1
        break
    else:
        f=s
        s=s+1
        ne=f*s
if c==0:
    print("NO")
        
    