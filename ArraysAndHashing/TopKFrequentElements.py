import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heap
        ans=[]
        #dict
        freq=dict()
        #iterate through all the numbers
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                freq[n]+=1
        for key,val in freq.items():
            if len(ans)<k:
                heapq.heappush(ans,[val,key])
            else:
                heapq.heappushpop(ans,[val,key])
        return [key for value,key in ans]




