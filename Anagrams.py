s1=input().lower()
x=set(s1)
s2=input().lower()
y=set(s2)
s=[]
c=0
for i in x:
    if i not in y:
        s.append(i)
        c+=1
if c==0:
    print(True)
else:
    print(False)