n = int(input())
f,s =0,1
print(f,s ,end = " " )
ne=f+s
n-=2
while n:
    n -=1
    print(ne, end = " ")
    f=s
    s=ne
    ne=f+s