n = int(input())
lst = list(map(int, input().split()))
c=0
x = []
for i in lst:
    if i%2==0 and i not in x:
        x.append(i)
for i in x:
    c+=i
print(c)