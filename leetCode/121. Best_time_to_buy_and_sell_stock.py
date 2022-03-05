
def maxProfit(prices):
    result = -100000000
    for i in range(0, len(prices)-1):
        for j in range(i+1, len(prices)):
            value = prices[j]-prices[i]
            if value >= result:
                result = value

    if result < 0:
        return 0
    else:
        return result


print(maxProfit([7,1,5,3,6,4]))

# 답은 맞는데 시간초과가 걸림. (입력 데이터 10**5개)
