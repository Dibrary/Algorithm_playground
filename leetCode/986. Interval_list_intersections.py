
def test(firstList, secondList):
    if firstList == [] or secondList == []: return []

    lower = min(min(min(firstList, secondList)))
    upper = max(max(max(firstList, secondList)))

    first_result, second_result = set(),set()
    for i in range(lower, upper+1):
        for k in firstList:
            if k[0]<= i <= k[1]:
                first_result.add(i)
        for l in secondList:
            if l[0]<= i <= l[1]:
                second_result.add(i)
    result = list(first_result&second_result)
    # 리스트로 어떻게 다시 묶느냐가 관건.
