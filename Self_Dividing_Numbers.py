a = int(input())
b = int(input())
for i in range(a,b+1):
    a=i
    cnt=0
    d=0
    while a:
        if a%10!=0 and i %(a%10)==0:
            cnt += 1
        d +=1
        a //=10
    if cnt ==d:
        print(i,end = " ")
        