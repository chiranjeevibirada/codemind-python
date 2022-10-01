t,se,b = map(int,input().split())
c=2*se*t*b*512
x =c//1024
print("{}KB".format(x))