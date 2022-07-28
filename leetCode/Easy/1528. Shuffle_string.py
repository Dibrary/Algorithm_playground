'''
주어진 문자를, indices값의 위치에 따라 옮기기
'''

class Solution:
    def restoreString(self,s,indices):
        tmp = []
        for i in range(0, len(indices)):
            tmp.append((indices[i], s[i]))
        tmp.sort(key=lambda x: x[0])

        result = ""
        for i in tmp:
            result += i[1]
        return result

if __name__=="__main__":
    print(Solution().restoreString("codeleet",[4,5,6,7,0,2,1,3]))


