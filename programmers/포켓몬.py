def solution(nums):
    tmp = set(nums)
    if len(tmp) >= len(nums)//2:
        return len(nums)//2
    elif len(tmp) < len(nums)//2:
        return len(tmp)



## 다른 사람 코드 ##
def solution(ls):
    return min(len(ls)/2, len(set(ls)))




def solution(nums):
    return min(len(set(nums)), len(nums)//2)