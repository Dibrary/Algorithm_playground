'''
손님이 요청한 길이가 M일 때, M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을 구해보자.
'''

def test():
    print("떡의 갯수 와 길이를 입력해주세요.")
    n,m = [x for x in input().split()]
    n = int(n); m = int(m) # 정수로 변환함.

    Duks = [int(k) for k in input().split()]

    start_value = 0
    end_value = max(Duks)

    while start_value <= end_value:
        mid = int((end_value + start_value)/2)
        sum_length = 0
        for i in Duks:
            if i > mid:
                sum_length += (i-mid)

        if sum_length == m: return mid
        elif sum_length > m:start_value = mid+1
        else:               end_value = mid-1

    return -1

if __name__=="__main__":
    print(test())

