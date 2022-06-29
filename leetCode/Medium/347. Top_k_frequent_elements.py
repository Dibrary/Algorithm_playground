import collections


class Solution:
    def topKFrequent(self, nums, k):
        result = [ x for x in set(nums) if nums.count(x) >= k]
        return result


k = Solution()
# k.topKFrequent([1,1,1,2,2,3],2)
# k.topKFrequent([1],1)
print(k.topKFrequent([1,2],2)) # 여기서 []가 나오는데 답은 [1,2] 가 나와야 한다고 함;;

'''
상위 k번 이상 나오는 숫자를 추출해야 하는 것.

'''

### 책 풀이 ###
from collections import Counter # Counter를 쓰면 한 번에 값이 key로, 빈도수가 value로 들어간 해시를 만든다.
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freqs = Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk


class Solution:
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]