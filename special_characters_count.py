s=input()
c=0
for i in s:
    if (i>='a' and i<='z') or (i>="A" and i<="Z") or i==' ':
        pass
    else:
        c+=1
print(c)