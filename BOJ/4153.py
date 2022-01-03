
while True:
    nums = list(map(int, input().split()))

    if nums == [0,0,0]: break

    nums.sort()
    max_value = nums.pop()
    others_length_sum = nums[0]*nums[0] + nums[1]*nums[1]
    if max_value*max_value == others_length_sum:
        print("right")
    else:
        print("wrong")