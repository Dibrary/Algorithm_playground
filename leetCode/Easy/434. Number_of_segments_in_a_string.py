'''
공백만 제거한 길이를 반환하자.
'''


class Solution:
    def countSegments(self, s):
        tmp = s.split(" ")

        if set(tmp) == {""}:
            return 0
        else:
            cnt = 0
            for i in tmp:
                if i != "":
                    cnt += 1

            return cnt

if __name__=="__main__":
    k = Solution()
    print(k.countSegments("Of all the gin joints in all the towns in all the world,   "))