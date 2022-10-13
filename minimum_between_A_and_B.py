n = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())
x = []
for i in lst:
    if i >= a and i <= b:
        x.append(i)

if len(x) == 0:
    print(-1)
else:
    print(min(x))