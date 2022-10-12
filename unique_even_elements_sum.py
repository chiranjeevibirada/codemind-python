n = int(input())
lst = list(map(int, input().split()))
x = []
s=0
for i in lst:
    if i%2==0 and i not in x:
        x.append(i)
for i in x:
    s+=i
print(s)