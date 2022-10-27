s=input()
c=0
x=0
y=len(s)-1
while x<y:
    if (s[x] in 'aeiouAEIOU' and s[y] not in 'aeiouAEIOU' and s[x]!=' ' and s[y]!=' ') or (s[x] not in 'aeiouAEIOU' and s[y] in 'aeiouAEIOU' and s[x]!=' ' and s[y]!=' '):
        c+=1
    x+=1
    y-=1
print(c)