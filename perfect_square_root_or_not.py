n = int(input())
i=1
c=0
while i<=n:
    if (i*i)==n:
        print("True")
        c=1
        break
    i+=1
if c==0:
    print("False")
    