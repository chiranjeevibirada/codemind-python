s = input()
x=[]
for i in range(len(s)):
    d = 0
    x.append(s[i])
    for j in x:
        if j in 'aeiouAEIOU':
            d+=1
print(d)