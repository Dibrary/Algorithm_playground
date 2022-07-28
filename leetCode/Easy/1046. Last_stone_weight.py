class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:
            first, second = max(stones), \
            max(stones[:stones.index(max(stones))]+stones[stones.index(max(stones))+1:])

            if first > second:
                stones[stones.index(first)] = first-second
                stones.remove(second)
            elif first == second:
                stones.remove(first)
                stones.remove(second)
            else:
                stones[stones.index(second)] = second-first
                stones.remove(first)
        if stones == []: # leetcode의 단점은 이런 출력에 대해 어떻게 처리해야될지 처음부터 알려주지 않음 ;;
            return 0
        else:
            return stones[0]