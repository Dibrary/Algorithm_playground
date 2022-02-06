
n, w, h, l = map(int, input().split())

a = w//l
b = h//l

tmp = a*b

if n >= tmp:
    print(tmp)
else:
    print(n)

