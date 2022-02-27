def typeChange(total_hour, total_min):

    total_hour = str(total_hour)
    total_min = str(total_min)
    total_mins = ""
    if total_hour == 1: # 여기에 len을 안 써서 조건문이 적용 안 되었음.
        total_hour = "0"+total_hour
    if total_min == 1:
        total_mins = "0"+total_min
    return total_hour, total_min

while True:
    a, b = input().split()
    if a == "00:00" and b == "00:00":
        break
    a_hour, a_min = map(int, a.split(":"))
    b_hour, b_min = map(int, b.split(":"))

    total_hour, total_min = a_hour+b_hour, a_min+b_min
    if total_min >=60:
        total_hour = total_min//60
        total_min = total_min%60
        print(total_hour, total_min, "1차")

    tip = 0
    if total_hour >= 24:
        tip = total_hour//24
        total_hour %= 24
        print(total_hour, total_min, "2차")

    total_hour = str(total_hour)
    total_min = str(total_min)

    if len(total_hour) == 1:
        total_hour = "0"+total_hour
    if len(total_min) == 1:
        total_min = "0"+total_min

    if tip == 0:
        print("%s:%s"%(total_hour, total_min))
    else:
        print("%s:%s +%d" %(total_hour, total_min, tip))
