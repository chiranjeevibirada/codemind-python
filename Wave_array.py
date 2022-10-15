n = int(input())
lst=list(map(int,input().split()))
c=0
d=0
if lst[0]<lst[1]:
    for i in range(n-1):
        if i%2==0:
            if lst[i]<lst[i+1]:
                c+=1
            else:
                print("no")
                break
        else:
            if lst[i]>lst[i+1]:
                c+=1
            else:
                print("no")
                break
    if (c+1)==n:
        print("yes")
else:
    for i in range(n-1):
        if i%2==0:
            if lst[i]>lst[i+1]:
                c+=1
            else:
                print("no")
                break
        else:
            if lst[i]<lst[i+1]:
                c+=1
            else:
                print("no")
                break
    if (c+1)==n:
        print("yes")