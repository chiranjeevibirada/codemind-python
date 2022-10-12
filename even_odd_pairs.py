n = int(input())
lst = list(map(int, input().split()))
e = []
o = []
for i in lst:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
if len(e) > len(o):
    p = len(o)
    res = e[p:]
else:
    p = len(e)
    res = o[p:]
for i in range(p):
    print(e[i], o[i], end = ' ')

for i in res:
    print(i, end = ' ')
if (len(res) % 2 == 1):
    print(0)