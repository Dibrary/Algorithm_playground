class Solution:
    def sortByBits(self, arr):
        tmp = []
        for i in arr:
            value = bin(i)[2:]
            tmp.append((i, value.count("1")))

        tmp.sort(key=lambda x: (x[1], x[0]))
        result = []
        for k in tmp:
            result.append(k[0])
        return result
