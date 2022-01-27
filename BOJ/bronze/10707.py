

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

a_price = a*p
b_price = 0
if p <= c:
    b_price = b
elif p > c:
    b_price = b+(p-c)*d

if a_price >= b_price:
    print("%d"%(b_price))
else:
    print("%d"%(a_price))







