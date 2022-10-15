n=int(input())
lst=list(map(int,input().split()))
#print(li)
for i in lst:
    print(len(str(abs(i))),end=" ")