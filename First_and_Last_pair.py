n = int(input())
lst = list(map(int, input().split()))
# for i in range(n // 2):
#     print(lst[i], lst[n - 1 - i], end = ' ')
# if n % 2 == 1:
#     print(lst[n//2], 0)

i = 0
j = n - 1
while i < j:
    print(lst[i], lst[j], end = ' ')
    i += 1
    j -= 1
if n % 2 == 1:
    print(lst[i], 0)
