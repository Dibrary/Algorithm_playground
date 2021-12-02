'''
달팽이 문제
'''

# 이 문제의 관건은, 맨 마지막에 낮에 올라갔을 때 정상을 돌파하면? 내려오지 않는걸로 간주해서 -B를 하지 않는다는 것.

import math
A, B, V = list(map(int, input().split()))
print(math.ceil((V-A)/(A-B)+1))

# 단순히 (A-B)x >= V 이런 부등식으로 풀려했다가 결과값이 안맞음.