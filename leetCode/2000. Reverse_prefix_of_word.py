'''
주어진 문자열에서, 특정 글자가 주어질 때,
해당 글자 앞부분의 모든 내용을 역순으로 하고 그 뒤의 나머지 문자열은 그대로 출력한다.
'''

class Solution:
    def reversePrefix(self, word, ch):
        tmp = ''
        idx = 0
        for i in range(0, len(word)):
            if word[i] != ch:
                tmp += word[i]
            else:
                tmp += word[i]
                idx = i
                break

        result = ''
        if idx == 0 and len(tmp) == len(word):
            return tmp
        else:
            result = tmp[::-1] + word[i+1:]
            return result

if __name__=="__main__":
    k = Solution()
    print(k.reversePrefix("abcdefd", "d"))
    print(k.reversePrefix("xyxzxe", "z"))
    print(k.reversePrefix("abcd", "z"))
    print(k.reversePrefix("xxxxxxxxx", "x"))