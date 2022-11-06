
'''
food로 주어진 숫자는 index의 값 '갯수'를 의미하는듯 하다.
0은 항상 1개 있다.

'''

def solution(food):
    dic = {"0":1}

    for x in range(1, len(food)):
        if food[x]%2 == 0:
            dic[x] = food[x]
        elif food[x] >= 3 and food[x]%2 == 1:
            dic[x] = food[x]-1 # 짝수개만 담게 함
    print(dic)


print(solution([1,3,4,6]))
print(solution([1,7,1,2]))



