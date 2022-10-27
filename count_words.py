s=list(map(str,input().split()))
n = len(s)
c=0
for i in s:
        if i[0] in "aeiouAEIOU" and i[len(i)-1] not in 'aeiouAEIOU' :
            c+=1
print(c)