n,m = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
cnt = 0
for i in a:
    if i not in b:
        cnt += 1

for i in b:
    if i not in a:
        cnt += 1
print(cnt)