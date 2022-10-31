s1=input().lower()
s2=input().lower()
x=[]
v=''
w=''
if len(s2)>len(s1):
    s1,s2=s2,s1
for i in s1:
    if i.isalpha() and i not in s2 and i not in x:
        x.append(i)
        v+=i
for i in s2:
    if i.isalpha() and i not in s1 and i not in x:
        x.append(i)
        v+=i
v=sorted(v)
for i in v:
    w+=i
print(w)