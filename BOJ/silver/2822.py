
score = []
for i in range(1,9):
    score.append((i,int(input())))
score.sort(key=lambda x:x[1])

problems = []
total = 0
for i in score[-5:]:
    problems.append(i[0])
    total += i[1]
problems.sort()
result = ""
for i in problems:
    result += str(i)+" "
print("%d"%(total))
print("%s"%(result[:-1]))





