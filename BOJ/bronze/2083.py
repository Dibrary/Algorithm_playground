# while True:
#     name, age, weight = list(input().split())
#     age, weight = int(age), int(weight)
#
#     if name == "#" and age == 0 and weight == 0:
#         break
#     elif age > 17 or weight > 80:
#         print("%s Senior" % (name))
#     else:
#         print("%s Junior" % (name))
#
# 틀림

# while True:
#     name, age, weight = input().split()
#     if name == "#" and age == "0" and weight == "0":
#         break
#     else:
#         if int(age) > 17 or int(weight) > 80:
#             print(f"{name} Senior")
#         elif int(age) <= 17 and int(weight) <= 80:
#             print(f"{name} Junior")

# 50% 에서 틀린다고 나옴


while True:
    name, age, weight = input().split()
    if name == "#" and age == "0" and weight == "0":
        break
    else:
        if int(age) > 17 or int(weight) > 79: # 80 이상부터 이므로 80은 포함된다.
            print(f"{name} Senior")
        else:
            print(f"{name} Junior")