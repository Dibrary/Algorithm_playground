
def solution(age):
    result = ''
    for x in age:
        result += str(chr(int(x)+97))
    return result


print(solution('23'))
print(solution('51'))

print(ord('a'))
print(('a'))



## 다른 사람 코드 ##

def solution(age):
    return ''.join([chr(ord('a')+int(i)) for i in str(age)])




