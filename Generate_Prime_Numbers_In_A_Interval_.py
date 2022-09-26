n = int(input())
m = int(input())
c=0
for i in range(n,m+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                c=1
                break
        else:
            print(i)

    