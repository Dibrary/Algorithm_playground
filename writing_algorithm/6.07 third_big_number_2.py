'''
3번째로 큰 수를 반환하자.
입력 값이 3개보다 작다면, 큰 수를 반환하자.
입력 값에는 중복이 있을 수 있다. 중복이 있다면, 갯수와 관계 없이 크기로만 3번째 값을 반환해보자.
'''

def test():
    print("input array")
    nums = [int(x) for x in input().split()]
    num_list = list(set(nums))

    return num_list[-3] if len(num_list) > 3 else max(num_list)

if __name__=="__main__":
    print(test())