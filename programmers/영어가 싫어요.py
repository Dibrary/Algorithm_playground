
def solution(numbers):
    table = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    value = ['0','1','2','3','4','5','6','7','8','9']

    for t, v in zip(table, value):
        numbers = numbers.replace(t, v)
    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))


## 다른 사람 코드 ##

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)





def solution(numbers):
    num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, word in enumerate(num_words):
        numbers = numbers.replace(word, str(num))
    return int(numbers)