n = int(input())
f,s =0,1
ne = f+s
while ne<=n:#8<=5
    f=s     #3
    s=ne    #5
    ne =f+s  #8
if n==s:
    print("True")
else:
    print("False")