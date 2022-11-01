def rev(x):
  return x[::-1]
s=input().lower()
if rev(s)==s:
    print(True)
else:
    print(False)