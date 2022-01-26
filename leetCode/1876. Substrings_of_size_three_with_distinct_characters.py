class Solution:
    def countGoodSubstrings(self, s):
        tmp = []

        for i in range(0, len(s)-2):
            if len(set(s[i:i+3])) == 3:
                tmp.append(s[i:i+3])
        return len(tmp)