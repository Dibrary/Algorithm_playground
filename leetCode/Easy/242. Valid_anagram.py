class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s);
        t = list(t)

        if len(s) > len(t):
            first = t
            second = s
        else:
            first = s
            second = t

        for i in first:
            if i in second:
                second.remove(i)
        return True if len(second) == 0 else False


### 다른 사람 코드 ###

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = string.ascii_lowercase
        for letter in letters:
            if s.count(letter) == t.count(letter):
                if len(s) == len(t):
                    if set(s) == set(t):
                        return True
            else:
                return False




### 책 풀이 ####

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)






