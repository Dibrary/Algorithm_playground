k = int(input())

a_values, b_values = [],[]
for _ in range(k):
    a, b = input().split(",")
    a_values.append(a)
    b_values.append(b)

print("%d,%d"%(int(min(a_values))-1,int(min(b_values))-1))
print("%d,%d"%(int(max(a_values))+1,int(max(b_values))+1))