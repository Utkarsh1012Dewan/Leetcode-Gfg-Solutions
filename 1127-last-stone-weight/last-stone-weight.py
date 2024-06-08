from heapq import heapify,heappush,heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return max(stones) - min(stones)

        stones = [-x for x in stones]
        heapify(stones)

        while True:
            if len(stones) <=1:
                break
            y = heappop(stones)
            x = heappop(stones)

            if x != y:
                heappush(stones,y-x)
            else:
                continue

        return -stones[0] if len(stones) == 1 else 0
