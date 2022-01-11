class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"

        f, s, t = 0, 0, 0
        result = []

        for i in words:
            if len(i) == 1:
                result.append(i)
                continue
            for idx, k in enumerate(i):
                k = k.lower()
                if idx == 0:
                    if k in first:   f = 1
                    if k in second:  s = 1
                    if k in third:   t = 1
                if f == 1 and k not in first:
                    break
                elif s == 1 and k not in second:
                    break
                elif t == 1 and k not in third:
                    break
                if idx == len(i) - 1:
                    result.append(i)
            f, s, t = 0, 0, 0 # 이게 없어서 중간 테스트 케이스들 모두 에러남.
        return result