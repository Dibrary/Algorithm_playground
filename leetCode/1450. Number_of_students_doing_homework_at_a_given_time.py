
def test(startTime, endTime, queryTime):
    cnt = 0
    for i in range(0, len(startTime)):
        if startTime[i]<= queryTime and endTime[i]>=queryTime:
            cnt += 1
    return cnt