s=input().split()
x=[]
a=0
b=0
for i in s:
    a += ord(min(i))
    b += ord(max(i))
print(b-a)