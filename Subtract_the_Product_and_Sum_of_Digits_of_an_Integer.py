n = int(input())
c=0
s =0
p=1
while n>0:
    c = n%10
    n = n//10
    s += c
    p *= c
print(p-s)
    
    