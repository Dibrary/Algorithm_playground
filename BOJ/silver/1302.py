n = int(input())

books = []
count = []
for _ in range(n):
    book = input()
    if book not in books:
        books.append(book)
        count.append(1)
    else:
        count[books.index(book)] += 1

result = []
max_cnt = max(count)

for idx, i in enumerate(books):
    if count[books.index(i)] == max_cnt:
        result.append(i)
result.sort()
print("%s"%(result[0]))