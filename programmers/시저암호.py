
def solution(s, n):
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table2 = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for i in s:
        if i == " ":
            result += " "
        elif i.isupper():
            tmp = ord(i)-65
            tmp += n
            if tmp >= 26:
                tmp -= 26
                result += table[tmp]
            else:
                result += table[tmp]
        elif i.islower():
            tmp = ord(i)-97
            tmp += n
            if tmp >= 26:
                tmp -= 26
                result += table2[tmp]
            else:
                result += table2[tmp]
    return result


### 다른 사람 풀이 ###
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer

### 다른 사람 풀이 ###
def caesar(s, n):
    def inner(word):
        c = (lambda a: a+26 if 97>a else a-26 if a>122 else a)(ord(word.lower()) + (n%26))
        return chr(c).upper() if word.isupper() else chr(c)
    return "".join([inner(w) if w.isalpha() else w for w in list(s)])