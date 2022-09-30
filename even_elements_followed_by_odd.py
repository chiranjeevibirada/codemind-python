n = int(input())
x = list(map(int,input().split()))
l =[]
for i in range(n):
    if x[i]%2==0:
        l.append(x[i])
for i in range(n):
    if x[i]%2!=0:
        l.append(x[i])
for i in l:
    print(i,end = ' ')
    
    