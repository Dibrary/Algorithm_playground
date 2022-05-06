
n, m = map(int, input().split())

boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

for i in range(len(boxes)):
    for s in range(len(books)):
        if boxes[i] >= books[s]:
            boxes[i] -= books[s]
            books[s] = 0 # 0으로 안만들면 다음 for문에서 또 - 적용함.

print(sum(boxes))



