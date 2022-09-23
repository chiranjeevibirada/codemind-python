n = int(input())
l=[]
for i in range(2,n):
    if n%i==0:
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            l.append(i)
c=0
for i in range(0,len(l)-1):
    for j in range(1,len(l)):
        if l[i]*l[j]==n:
            c+=1
            print(l[i],l[j])
            break
if c==0:
    print(-1)
