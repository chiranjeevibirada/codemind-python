n = int(input())
l = list(map(int,input().split()))
print(*l, end = ' ')
if n % 2 == 1:
    print('0')