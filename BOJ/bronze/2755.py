
n = int(input())

table = {"A+":4.3,"A0":4.0,"A-":3.7,
         "B+":3.3,"B0":3.0,"B-":2.7,
         "C+":2.3,"C0":2.0,"C-":1.7,
         "D+":1.3,"D0":1.0,"D-":0.7,
         "F":0.0}

total_score = 0
cnt = 0

for _ in range(n):
    name, score, grade = input().split()
    cnt += int(score)
    total_score += table[grade]*int(score)
print(total_score, cnt)
print("{:.2f}".format(total_score/cnt)) # 문제는 소수점 표시다.