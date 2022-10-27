r=input()
s=r.split()
x=[]
for i in s:
    x.append(min(i))
    x.append(max(i))
print(min(x),r.count(min(x)),max(x),r.count(max(x)))