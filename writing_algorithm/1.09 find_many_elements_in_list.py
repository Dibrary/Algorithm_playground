'''
정수형 배열이 주어질 때, 다수의 요소를 찾자.
다수의 수는 무조건 하나만 존재한다고 가정.
'''


def test(params):
    components = list(set(params))
    length = len(params) / 2

    for i in range(0, len(components)):
        if params.count(components[i]) > length:
            return components[i]


if __name__=="__main__":
    print(test([1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,4,4]), test([1,1,1,1,1,1,1,2,2]))

