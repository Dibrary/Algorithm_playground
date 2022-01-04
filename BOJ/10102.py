n = int(input())
arr = input()
a_count = arr.count("A")
b_count = arr.count("B")
if a_count > b_count:
    print("A")
elif a_count < b_count:
    print("B")
else:
    print("Tie")