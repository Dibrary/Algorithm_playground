
n = input()

mid_idx = len(n)//2
left = n[:mid_idx]
right = n[mid_idx:]


left_sum = 0
for i in left:
    left_sum += int(i)
right_sum = 0
for j in right:
    right_sum += int(j)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

