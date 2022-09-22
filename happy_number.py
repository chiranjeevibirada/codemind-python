num = int(input())
sum = 0
while True:
    while num!=0:
        sum+=(num%10)**2
        num=num//10
    if sum==1 or sum==7:
        print("True")
        break
    elif sum<10:
        print("False")
        break
    else:
        num=sum
        sum=0