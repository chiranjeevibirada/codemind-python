n = int(input())
x = list(map(int,input().split()))
a,b = map(int,input().split())
c=0
for i in range(n):
    if x[i]<a or x[i]>b:
        print(x[i],end = ' ')
        c=1
if c==0:
    print('-1')
    
    