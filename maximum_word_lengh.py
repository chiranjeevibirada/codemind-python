s=input()
lst=s.split()
x=[]
for i in lst:
    x.append(len(i))
print(max(x))