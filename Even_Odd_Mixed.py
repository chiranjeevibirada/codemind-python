n = int(input())
c=0
Even =0
Odd =0
while n>0:
    c = n%10
    n=n//10
    if c%2==0:
        Even = Even+1
    else:
        Odd = Odd +1
if Even >0 and Odd ==0:
    print("Even")
elif Odd>0 and Even==0:
    print("Odd")
else:
    print("Mixed")
    
    
     
    