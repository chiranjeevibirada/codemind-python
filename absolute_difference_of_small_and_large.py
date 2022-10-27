s=input().split()
x=[]
for i in s:
    x.append(ord(max(i))-ord(min(i)))
print(*x)