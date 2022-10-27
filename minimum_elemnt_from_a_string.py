s=input().split()
s=s[-1]
r=min(s)
if r.lower() in s:
    print(r.lower())
else:
    print(min(s))