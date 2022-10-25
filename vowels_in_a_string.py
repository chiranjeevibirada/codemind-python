s=input()
v=input()
x=[]
for i in range(len(s)):
    x.append(s[i])
    if v in x:
        print(True)
        print(i)
        break
else:
    print(False)