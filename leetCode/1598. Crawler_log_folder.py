class Solution:
    def minOperations(self, logs):
        cnt = 0
        for i in logs:
            if "." not in i:
                cnt += 1
            elif i == "../":
                if cnt != 0:
                    cnt -= 1

        return 0 if cnt < 0 else cnt
