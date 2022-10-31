s1=input().lower()
s2=input().lower()
s1=s1.split()
s2=s2.split()
x=[]
c=0
if len(s2)>len(s1):
    s1,s2=s2,s1
for i in s1:
    if i in s2 and i not in x:
        x.append(i)
        c+=1
for i in s2:
    if i in s1 and i not in x:
        x.append(i)
        c+=1
print(c)