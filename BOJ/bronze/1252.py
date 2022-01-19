

a, b = input().split()
a = int("0b"+a, 2)
b = int("0b"+b, 2)
c = a+b
print("%d"%(int(bin(c)[2:])))