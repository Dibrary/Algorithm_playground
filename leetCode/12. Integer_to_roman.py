'''
정수를 다시 로마자로 표기하는 방법.
'''

class Solution:
    def intToRoman(self, target):
        tmp = [1,2,3,4,5,9,10,40,50,90,100,400,500,900,1000]
        mapping = {1:"I",
                   2:"II",
                   3:"III",
                   4:"IV",
                   5:"V",
                   9:"IX",
                   10:"X",
                   40:"XL",
                   50:"L",
                   90:"XC",
                   100:"C",
                   400:"CD",
                   500:"D",
                   900:"CM",
                   1000:"M"}

        start = 0
        end = len(tmp)-1

        result = []
        while target > 0:
            while start <= end:
                mid = int((end+start)//2)
                if tmp[mid] < target:
                    start = mid + 1
                elif tmp[mid] > target:
                    end = mid -1
                elif tmp[mid] == target:
                    result.append(tmp[mid])
                    target -= tmp[mid]

            result.append(tmp[start-1])
            target-= tmp[start-1]
            start = 0
            end = len(tmp)-1

        string = ""
        for i in result[:len(result)-1]:
            string += mapping[i]
        return string


if __name__=="__main__":
    k = Solution()
    print(k.intToRoman(58))
    print(k.intToRoman(1994))
