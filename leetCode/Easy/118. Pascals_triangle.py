'''
파스칼 삼각형 계수 구하기
'''

class Solution:
    def generate(self, k):
        if k == 1:
            return [[1]]
        elif k == 2:
            return [[1], [1, 1]]  # 여기서 elif문 중에 k==1, 2인 경우는 한 개의 return문으로 종합할 수 있다.
        else:
            result = [[1], [1, 1]]
            cnt = 3
            while cnt <= k:
                tmp = []
                tmp.append(1)

                for i in range(1, cnt - 1):
                    tmp.append(result[cnt - 2][i - 1] + result[cnt - 2][i])
                tmp.append(1)
                result.append(tmp)
                cnt += 1
            return result

if __name__=="__main__":
    print(Solution().generate(1))