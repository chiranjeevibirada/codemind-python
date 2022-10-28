s= input()
v=[]
l=[]
z=""
j,k=0,0
for i in s:
    if (i >="a" and i<="z")or(i>="A" and i<="Z"):
            l.append(i)
    else:
        v.append(i)
l=sorted(l) 
for i in s:
    if i in l:
        z=z+l[j]
        j+=1
    else:
        z=z+v[k]
        k+=1
print(z)