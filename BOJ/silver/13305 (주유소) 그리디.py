
'''
최저 가격을 만난 순간부터 그 가격으로 나머지 거리를 모조리 가면 됨.
'''

# n = int(input())
# roads = list(map(int, input().split())) # 도로 길이
# soils = list(map(int, input().split())) # 주유소 리터당 가격
#
# total_price = 0
#
# for i in range(len(soils)):
#     if soils[i] == min(soils[:-1]):
#         total_price += soils[i]*sum(roads[i:])
#         break
#     else:
#         total_price += soils[i]*roads[i]
# print(total_price)

# 17점 맞았다 ;;

n = int(input())
roads = list(map(int, input().split())) # 도로 길이
soils = list(map(int, input().split())) # 주유소 리터당 가격

total_price = 0
min_price = 10000000001

for i in range(len(roads)):
    if min_price > soils[i]:
        min_price = soils[i]
        total_price += min_price*roads[i]
    else:
        total_price += min_price*roads[i]
print(total_price)

# 이렇게 수정하니 100%로 통과됨.




## 다른 사람 코드 ##

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = 0
m = costs[0] # 가장 작은 값으로 갱신되는 위치
for i in range(n-1):
    if costs[i] < m:
        m = costs[i]
    res += m * roads[i]
print(res)


