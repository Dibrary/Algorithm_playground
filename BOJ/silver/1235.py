
n = int(input())

students = []
for _ in range(n):
    students.append(input()[::-1])

tmp = set()
length = 1
while length < len(students[0]):
    for i in range(len(students)):
        tmp.add(students[i][:length])

    if len(tmp) == len(students):
        print(len(list(tmp)[0]))
        break
    tmp = set()
    length += 1

# 틀림, 2진탐색 해야되나?






