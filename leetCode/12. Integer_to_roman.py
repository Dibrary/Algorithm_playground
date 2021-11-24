'''
정수를 다시 로마자로 표기하는 방법.
'''

class Solution:
    def intToRoman(self, num):
        tmp = [4,9,10,40,50,90,100,400,500,900,1000]

        start = 0
        end = len(tmp) - 1

        result = []
        while start < end:
            mid = int((start - end) / 2)

            if num > mid:
                start = mid + 1
            elif num < mid:
                end = mid - 1
            else:
                result.append(tmp[mid])
        return result


if __name__=="__main__":
    k = Solution()
    print(k.intToRoman(58))
