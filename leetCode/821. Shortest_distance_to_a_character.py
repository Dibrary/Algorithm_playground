class Solution:
    def shortestToChar(self, s, c):

        dist = 20000

        result = []
        for i in s:
            if i != c:
                dist += 1
                result.append(dist)
            elif i == c:
                result.append(0)
                dist = 0

        dist = 0
        for k in range(len(s) - 1, -1, -1):
            if s[k] != c:
                dist += 1
                result[k] = min(result[k], dist)
            else:
                result[k] == 0
                dist = 0
        return result

# 양 끝단에서 예외가 발생한다.