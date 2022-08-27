
def solution(word):
    word = ['A', 'E', 'I', 'O', 'U']
    table = ['A','AA','AAA','AAAA','AAAAA']+[]
    for x in range(len(word)):
        for y in range(len(word)):
            for z in range(len(word)):
                for w in range(len(word)):
                    for m in range(len(word)):
                        table.append((word[x]+word[y]+word[z]+word[w]+word[m]))

# 이렇게 하려 했으나 아니다.
# 아마 AUUUU  뒤에 다시 E, EE, EEE, EEEE, EEEEE, EEEEI 이렇게 진행 될 듯.








