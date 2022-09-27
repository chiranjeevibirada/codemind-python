n = int(input())
x = list(map(int,input().split()))
avg = sum(x)/n
print("{:.2f}".format(avg))