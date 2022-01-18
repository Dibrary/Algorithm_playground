class Solution:
    def replaceWords(self, dictionary, sentence):
        sentence = list(sentence.split(" "))

        for k in dictionary:
            for idx, j in enumerate(sentence):
                if k == j[:len(k)]:
                    sentence[idx] = k
        return " ".join(map(str, sentence))

print(Solution().replaceWords(["cat","bat","rat"],"the cattle was ratted by the battery"))