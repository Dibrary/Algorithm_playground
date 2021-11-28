'''
주어진 리스트에서 1개의 값을 선택해 +1을 합니다.
그 결과, 모든 숫자의 곱이 가장 큰 경우, 해당 최대값을 반환하자.
'''

class Cryptography:
    def encrypt(self, numbers):
        result = 0
        for i in range(0, len(numbers)):
            sample = numbers.copy()
            sample[i] += 1
            tmp = 1
            for k in range(0, len(numbers)):
                tmp *= sample[k]
            if tmp > result:
                result = tmp
        return result


if __name__=="__main__":
    k = Cryptography()
    print(k.encrypt([1,2,3]))
    print(k.encrypt([1,3,2,1,1,3]))
    print(k.encrypt(([1,1,1,1])))
    print(k.encrypt([1000,999,998,997,996,995]))



