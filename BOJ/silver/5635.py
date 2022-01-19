
# n = int(input())
#
# old_name = ""
#
# old_name, day, month, year = input().split()
# old_day, old_month, old_year = int(day), int(month), int(year)
#
# for _ in range(n-1):
#     name, day, month, year = input().split()
#     day, month, year = int(day), int(month), int(year)
#     if year < old_year:
#         old_name = name
#         continue
#     elif year == old_year:
#         if month < old_month:
#             old_month = month
#             old_name = name
#             continue
#         elif month == old_month:
#             if day < old_day:
#                 old_day = day
#                 old_name = name
#                 continue
#             elif day == old_day:
#                 pass

# 위와같이 작성하다가 정렬을 쓸 수 있겠다 싶음.

n = int(input())

table = []
for _ in range(n):
    name, day, month, year = input().split()
    table.append((name,int(day), int(month), int(year)))

table.sort(key=lambda x:(x[3],x[2],x[1]))
print("%s"%(table[-1][0]))
print("%s"%(table[0][0]))








