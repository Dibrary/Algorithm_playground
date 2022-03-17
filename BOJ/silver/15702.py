
n, m = map(int, input().split())

students = dict()

scores = list(map(int, input().split()))

for _ in range(m):
    values = input().split()
    students[int(values[0])] = 0
    for j in range(len(values[1:])):
        if values[1:][j] == "O":
            students[int(values[0])] += scores[j]

max_value = max(students.values())
temp = []
for k in students:
    if students[k] == max_value:
        temp.append(k)
print(f'{min(temp)} {max_value}')


