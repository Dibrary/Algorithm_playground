
class Solution:
    def letterCombinations(self, digits):
        letters = {'2': ["a", "b", "c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"], '5': ["j", "k", "l"],
                   '6': ["m", "n", "o"], '7': ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9': ["w", "x", "y", "z"]}

        if digits == "":
            return []

        result = []
        if len(digits) == 1:
            for s in letters[digits[0]]:
                result.append(s)
            return result
        elif len(digits) == 2:
            for i in letters[digits[0]]:
                for j in letters[digits[1]]:
                    result.append(i + j)
            return result
        elif len(digits) == 3:
            for i in letters[digits[0]]:
                for j in letters[digits[1]]:
                    for k in letters[digits[2]]:
                        result.append(i + j + k)
            return result

        # 입력조건이 0 <= digits.length <= 4 이렇게 주어져서 그냥 for문 중첩으로 해결함. max를 계산 할 때 시간 내에 들어가서.
        elif len(digits) == 4:
            for i in letters[digits[0]]:
                for j in letters[digits[1]]:
                    for k in letters[digits[2]]:
                        for m in letters[digits[3]]:
                            result.append(i + j + k + m) # for문을 4번이나 쓰는데, 더 시간을 줄일 방법을 찾아보자.
            return result

print(Solution().letterCombinations("23"))