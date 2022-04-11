
n = int(input())

tmp = 0
op = ""

for i in range(2*n-1):
    value = input()
    if value.isdigit() and i == 0:
        tmp = int(value)
    elif value.isdigit() and i != 0:
        if op == "*":
            tmp *= int(value)
        elif op == "+":
            tmp += int(value)
        elif op == "-":
            tmp -= int(value)
        elif op == "/":
            tmp /= int(value)
    elif value.isdigit() == False:
        op = value # 연산자 등록

print(tmp)

# 아 +- 는 */ 보다 늦게 계산을 해야 됨 =_=;;

