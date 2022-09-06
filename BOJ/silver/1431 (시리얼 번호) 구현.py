
'''
"숫자가 알파벳보다 사전순으로 작다." 라는 문구가 뭔소린지 모르겠음.
위 숫자는 무조건 알파벳 보다 작으면 앞에 나와야 하지 않나? 예제 1번은 그렇지 않다.
'''

from collections import defaultdict

n = int(input())
table = defaultdict(list)
length = []

for _ in range(n):
    serial = input()
    if len(serial) not in length:
        length.append(len(serial))
    table[len(serial)].append(serial)

























