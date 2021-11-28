'''
공통 취미 갯수가 가장 높은 갯수를 찾자.
'''

class InterestingParty:
    def bestInvitation(self,first, second):
        tmp = dict()
        tag = list(set(first + second))

        for i in range(0, len(first)):
            if first[i] not in tmp: tmp[first[i]] = 1
            else:                   tmp[first[i]] += 1
            if second[i] not in tmp:tmp[second[i]] = 1
            else:                   tmp[second[i]] += 1

        result = 0
        for i in range(0, len(tmp)):
            if tmp[tag[i]] > result:
                result = tmp[tag[i]]
            else:
                pass
        return result

if __name__=="__main__":
    k = InterestingParty()
    print(k.bestInvitation(["f","g","s","f"], ["h","f","f","b"]))
    print(k.bestInvitation(["snakes","programming","cobra","monty"],["python","python","anaconda","python"]))