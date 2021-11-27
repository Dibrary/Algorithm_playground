'''
홀수 길이에 해당되는 모든 경우의 합 값을 구하자.
'''

class Solution:
    def odd_lengths(self):
        result = []
        for i in range(0, 101):
            if i%2 == 1:
                result.append(i)
        return result

    def sumOddLengthSubarrays(self, arr):
        tmp = odd_lengths()
        result = 0
        for i in tmp:
            for j in range(0, len(arr)):
                if j+i < len(arr):
                    result += sum(arr[j:i])
        return result

if __name__=="__main__":
    k = Solution()
    print(k.sumOddLengthSubarrays([1,4,2,5,3]))
