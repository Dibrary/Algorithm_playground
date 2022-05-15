
def length(value):
    result = None
    if len(value) != 6:
        result = (6-len(value))*"0"+value
        return result
    else:
        return value

def column_reading(h, m, s):
    result = ""
    for i in range(len(h)):
        result += h[i] # 세로로 하나씩 꺼내서 더한다.
        result += m[i]
        result += s[i]
    return result

n = int(input())

for _ in range(n):
    time_value = input().split(":")
    hour,min,sec = time_value[0], time_value[1], time_value[2]
    hour_value = length(bin(int(hour))[2:])
    min_value = length(bin(int(min))[2:])
    sec_value = length(bin(int(sec))[2:])

    column_result = column_reading(hour_value,min_value,sec_value)
    row_result = hour_value + min_value + sec_value # 그냥 가로로 더하기.

    print("%s %s"%(column_result, row_result))




