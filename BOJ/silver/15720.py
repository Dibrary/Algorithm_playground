
b, c, d = map(int, input().split())

burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

burgers.sort()
sides.sort()
drinks.sort()

total = sum(burgers) + sum(sides) + sum(drinks)
print(total)

# 이 밑에 할인 가능한 것은 할인 하고 더해야 한다.

discount_total = 0

min_count = min(b, c, d)
for i in range(min_count):
    tmp = 0
    tmp += burgers.pop(-1)
    tmp += sides.pop(-1)
    tmp += drinks.pop(-1)
    discount_total += (tmp*0.9)
result = discount_total + sum(burgers) + sum(sides) + sum(drinks)
print(int(result))
