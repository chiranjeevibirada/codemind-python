s = input()
s = s.split(' ')
x=[]
for i in range(len(s)):
    d = 0
    for j in s[i]:
        if j in 'aeiou':
            d+=1
    x.append(d)
print(max(x))