n = int(input())
lst =list(map(int,input().split()))
i=0
while i<=n:
    for j in range(lst[i+1]):
        print(lst[i],end = " ")
    i+=2