s=input()
s= s.split()
c=0
v="aeiouAEIOU"
for i in s:
    x=0
    y=len(i)-1
    while x<y:
        if i[x] in v and i[y] not in v:
            c+=1
        elif i[x] not in v and i[y] in v:
            c+=1
        x+=1
        y-=1
print(c)
        