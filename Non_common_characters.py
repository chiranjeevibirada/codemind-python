s1=input().lower()
s2=input().lower()
c=0
x=[]
if len(s2)>len(s1):
    s1,s2=s2,s1
for i in s1:
    if i.isalpha() and i not in s2 and i not in x:
        x.append(i)
        c+=1
for i in s2:
    if i.isalpha() and i not in s1 and i not in x:
        x.append(i)
        c+=1
print(c)