n = int(input())
x = list(map(int,input().split()))
avg = sum(x)//n
if avg in x:
    print(True)
else:
    print(False)