s = input()
s = s.split(' ')
x=[]
c=999999
for i in range(len(s)):
    d = 0
    for j in s[i]:
        if j in 'aeiou':
            d+=1
    x.append(d)
a=min(x)
print(x.count(a))