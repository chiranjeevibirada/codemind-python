n= int(input())
rev=0
while n:
    r = n%10
    n = n//10
    rev = rev*10+r
temp = 0
c=0
while rev:
    if rev%10==6 and c==0:
        c+=1
        temp=temp*10+9
    else:
        temp = temp*10+(rev%10)
    rev//=10
print(temp)