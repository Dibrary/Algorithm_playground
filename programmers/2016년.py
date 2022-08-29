
from datetime import date

def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return days[date(2016, a, b).weekday()]





## 다른 사람 코드 ##
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))













def getDayName(a,b):
    days = -1
    DAY = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    MONTH = {}
    MONTH[0] = 0

    for month in range(1, 13):
        if month == 2:
            MONTH[month] = 29
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            MONTH[month] = 31
        elif month in [4, 6, 9, 11]:
            MONTH[month] = 30

    for mon in range(a):
        days += MONTH[mon]
    days += b

    return DAY[days % 7]