s = input()
c = 0
d = "aeoiuAEIOU"
x = []
for i in s:
    if i in d:
        if i not in x:
            x.append(i)
        c+=1
if c==0:
    print("-1")
else:
    print(*x)