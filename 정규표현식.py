
import re
sentence = "가나다라마바사아자차카타파하"
string = re.compile("마바") # 정규표현식 패턴 객체로 변경한 것.

print(string.match(sentence)) # None
print(string.search(sentence)) # 0부터 시작해서 4~6에 있다고 알려줌.
# match는 문자열 시작부터 패턴을 탐색하지만, search는 모든 문자열 위치에 대해 탐색한다.

print(string.findall(sentence))


print(string.search(sentence).group()) # 일치하는 문자열 반환
print(string.search(sentence).start(), string.search(sentence).end()) # 시작, 끝 위치 반환
print(string.search(sentence).span()) # 시작과 끝 위치를 tuple로 반환.

'''
정규표현식의 핵심은 meta 문자.

특수 역할을 하는 [ ] , \ * + 등등 메타문자가 있다.

메타 문자	 역할
[ ]	[ ] 사이의 문자들과 매치. '-'으로 문자의 범위 표현 가능
.	줄바꿈(\n)을 제외한 모든 문자와 매치
\	이스케이프 처리 또는 숫자, 문자 집합 표현(\d, \s 등)
*	바로 앞에 있는 문자가 0부터 무한 번까지 반복
+	바로 앞에 있는 문자가 1부터 무한 번까지 반복
{m, n}	바로 앞에 있는 문자 m~n번 반복
?	{0, 1}과 동일
|	or과 동일 (A|B - A 또는 B를 찾아라)
^	문자열의 맨 처음과 일치함
$	문자열의 맨 끝과 일치함

'''


sentence = "My phone number is 010-2451-7878 and my age is 31."

# [abcd] : a, b, c, d 중에 매칭되는 한 개 탐색, [a-d]와 동일
print(re.compile("[abcd]").search(sentence)) # <re.Match object; span=(12, 13), match='b'> 시작 문자가 b다.

# [a-z] : 소문자, [A-Z] : 대문자, [a-zA-Z] : 알파벳 전체, [0-9] : 숫자
print(re.compile("[0-9]").search(sentence)) # <re.Match object; span=(19, 20), match='0'> 3 시작 숫자가 0이다.

# a.e : a + 모든 문자 + e (예, age, ace, a2e a1e 등)
re.compile("a.e").search(sentence) # <re.Match object; span=(40, 43), match='age'>

# \
# 이스케이프 처리, 숫자/문자 집합 표현

# 메타 문자를 이스케이프 시켜서 탐색 가능하게 한다.
re.compile("\(").search("[]()") # <re.Match object; span=(2, 3), match='('>

# \d : 숫자와 매치, [0-9]와 동일
# \D : 숫자가 아닌 것과 매치
# \s : 공백과 매치
# \S : 공백이 아닌 것과 매치
# \w : 문자 + 숫자와 매치, [a-zA-Z0-9_]와 동일
# \w : 문자 + 숫자가 아닌 것과 매치
re.compile("\d").search(sentence) # <re.Match object; span=(19, 20), match='0'>
re.compile("\D").search(sentence) # <re.Match object; span=(0, 1), match='M'>
re.compile("\s").search(sentence) # <re.Match object; span=(2, 3), match=' '>

# *
# 바로 앞에 있는 문자가 0부터 무한 번 반복

# a*b : a가 0부터 무한 번 반복 (예, b, ab, aab, aaab, aaaaaaab 등)
re.compile("a*b").search("aaaaaaaaaab") # <re.Match object; span=(0, 11), match='aaaaaaaaaab'>

# +
# 바로 앞에 있는 문자가 1부터 무한 번 반복

# a+b : a가 1부터 무한 번 반복 (예, ab, aab, aaaab 등) - b는 안됨
re.compile("a+b").search("ab") # <re.Match object; span=(0, 2), match='ab'>
re.compile("a+b").search("b") # None

# {}
# {m,n} : 앞에 문자가 m ~ n 번 반복
# {1,} : +와 동일, {0,} : *와 동일, {m,} : 반복 횟수 m ~ 무한대, {,n} : 반복 횟수 0~n

# a{2}b : a를 무조건 2번 반복
re.compile("a{2}b").search("ab") # None
re.compile("a{2}b").search("aab") # <re.Match object; span=(0, 3), match='aab'>

# a{3,}b : a를 3번 이상 반복
re.compile("a{3,}b").search("aab") # None
re.compile("a{3,}b").search("aaaaaaaab") # <re.Match object; span=(0, 9), match='aaaaaaaab'>

# ?
# {0,1}과 동일 : 앞에 문자가 0 ~ 1 번 반복

# ab?e : b가 0번 또는 한 번 반복
re.compile("ab?c").search("abc") # <re.Match object; span=(0, 3), match='abc'>
re.compile("ab?c").search("abbc") # None

# |
# or과 동일 A|B : A 또는 B 와 매치

# dog|cat : 개 또는 고양이와 매치
re.compile("dog|cat").search("that dog is so fast") # <re.Match object; span=(5, 8), match='dog'>
re.compile("dog|cat").search("that cat is so fast") # <re.Match object; span=(5, 8), match='cat'>

# ^
# 문자열의 맨 처음과 일치
re.compile("^dog").search("dog is not a cat") # <re.Match object; span=(0, 3), match='dog'>
re.compile("^dog").search("that dog is so fast") # None

# $
# 문자열의 맨 끝과 일치
re.compile("dog$").search("I like that dog") # <re.Match object; span=(12, 15), match='dog'>
re.compile("dog$").search("I like that dog, but i dont like that") # None




import re
# 0-9가 0개 이상인지 판단
print(re.match('[0-9]*','123')) # <re.Match object; span=(0, 3), match='123'>
print(re.match('[0-9]*','abc')) # <re.Match object; span=(0, 0), match=''>

# a-z가 1개 이상인지 판단
print(re.match('[a-z]+','abc')) # <re.Match object; span=(0, 3), match='abc'>

# 여러 문자 숫자 조합도 가능
print(re.match('[a-zA-Z0-9]+', 'Hello1234')) # <re.Match object; span=(0, 9), match='Hello1234'>
print(re.match('[A-Z0-9]+', 'hello')) # None
print(re.match('[$()a-zA-Z0-9]+', '$(document)')) # <re.Match object; span=(0, 11), match='$(document)'>

# 다음과 같이 활용 가능
# 문자열에서 a위치에 a가 0개 이상인지
print(re.match('a*b','b')) # <re.Match object; span=(0, 1), match='b'>
# 문자열에서 a위치에 a가 1개 이상인지
print(re.match('a+b','aab')) # <re.Match object; span=(0, 3), match='aab'>

print(re.match('abc?','abcd')) # <re.Match object; span=(0, 3), match='abc'>
print(re.match('ab[0-9]?c','ab3c')) # <re.Match object; span=(0, 4), match='ab3c'>

# . 있는지 위치에 문자(숫자)가 있는지 확인
print(re.match('ab.c','abc')) # None
print(re.match('ab.c','abxc')) # <re.Match object; span=(0, 4), match='abxc'>

# 문자{개수}, (문자열){개수} : 해당하는 문자(문자열)의 개수가 맞는지 판단
print(re.match('h{3}','hhhhhello')) # <re.Match object; span=(0, 3), match='hhh'>
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000')) # <re.Match object; span=(0, 13), match='010-1000-1000'>

# [^범위] : 해당 범위를 제외한 나머지
# ^[범위] : 해당 범위로 시작하지는지 판단
print(re.search('[^A-Z]+', 'Hello')) # <re.Match object; span=(1, 5), match='ello'>
print(re.search('^[A-Z]+', 'Hello')) # <re.Match object; span=(0, 1), match='H'>








