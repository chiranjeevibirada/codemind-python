a = "AEIOU"
b = "aeiou"
u = 0
l = 0
x= []
y= []
s = input()
for i in range(0,len(s)-1):
    if s[i] in a:
        if s[i] not in x:
            x.append(s[i])
            u+=1
    if s[i] in b:
        if s[i] not in y:
            y.append(s[i])
            l+=1
if u==5 or l==5:
    print(True)
else:
    print(False)