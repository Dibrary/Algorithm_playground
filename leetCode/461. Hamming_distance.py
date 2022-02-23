class Solution:
    def hammingDistance(self, x, y):
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        if len(x_bin) > len(y_bin):
            y_bin = "0" * (len(x_bin) - len(y_bin)) + y_bin

        elif len(x_bin) < len(y_bin):
            x_bin = "0" * (len(y_bin) - len(x_bin)) + x_bin

        cnt = 0
        for i in range(0, len(x_bin)):
            if x_bin[i] != y_bin[i]:
                cnt += 1
        return cnt