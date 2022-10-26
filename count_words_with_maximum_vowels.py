s = input()
s = s.split(' ')
x=[]
c=0
for i in range(len(s)):
    d = 0
    for j in s[i]:
        if j in 'aeiou':
            d+=1
    if d>c:
        c=d
        r=1
    elif d==c:
        r+=1
print(r)
