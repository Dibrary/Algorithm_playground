number = int(input())

for i in range(number):
    n, *nums = list(map(int, input().split()))
    average = (sum(nums)/n)
    cnt = 0
    for i in nums:
        if i > average:
            cnt += 1
    result = str(round((cnt/n)*100,3))
    if result[-1] == "0":
        result += "00"
    print(result+"%")

'''
틀렸다고 뜨는데, 왜 그런지 영문을 모름. 출력에 %를 추가해서 그런가..?
'''