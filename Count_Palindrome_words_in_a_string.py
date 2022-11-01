def rev(x):
    return x[::-1]
s=input().lower()
r=s.split()
c=0
for i in r:
    if rev(i)==i:
        c+=1
print(c)