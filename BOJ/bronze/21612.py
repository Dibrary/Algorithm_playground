
n = int(input())
p = 5*n-400

index = 0
if p < 100:
    index = 1
elif p > 100:
    index = -1
else:
    index = 0
print(p)
print(index)