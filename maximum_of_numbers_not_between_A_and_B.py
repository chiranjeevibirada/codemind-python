n = input()
x = list(map(int,input().split()))
a,b = map(int,input().split())
ma = -1
for i in x:
    if i<a or i>b:
        if ma<i:
            ma=i
print(ma)