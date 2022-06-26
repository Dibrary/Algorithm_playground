'''
로마자 순서대로 값을 아라비아 숫자로 나타내자.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

반드시 왼쪽의 값이 오른쪽 보다 커야 하며, 역순일 경우 차가 해당 값이 된다.
예) IV = 1이 5보다 앞에 있으므로, 5-1 = 4가 된다.
CM = 100이 1000보다 작은데 앞에 있으므로, 1000-100 = 900이 된다.
'''

class Solution:
    def romanToInt(self, s):
        mapping = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1, "N": 0}
        s += "N" # while루프 끝까지 돌기 위해 추가 함.
        cnt = 0
        result = 0

        while cnt < len(s) - 1:
            if mapping[s[cnt]] >= mapping[s[cnt + 1]]:
                result += mapping[s[cnt]]
                cnt += 1
            else:
                result += abs(mapping[s[cnt]] - mapping[s[cnt + 1]])
                cnt += 2
        return result

if __name__=="__main__":
    k = Solution()
    print(k.romanToInt('MCMXCIV'))