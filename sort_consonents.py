s= input().split()
for i in s:
    v = []
    l = []
    z = ""
    j,k=0,0
    for m in i:
        if m not in "aeiouAEIOU":
            l.append(m)
        else:
            v.append(m)
    l=sorted(l) 
    for p in i:
        if p in l:
            z=z+l[j]
            j+=1
        else:
            z=z+v[k]
            k+=1
    print(z, end = ' ')