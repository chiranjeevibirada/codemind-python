n = int(input())
l = list(map(int,input().split()))
c=0
x=[]
for i in l:
    if i not in x:
        x.append(i)
for i in x:
    if i>0:
        c+=i
print(c)