class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #creating a max heap from minheap cause python doesn't support maxheaps
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if second>first:
                heapq.heappush(stones,first-second)
        stones.append(0)
        return abs(stones[0])
