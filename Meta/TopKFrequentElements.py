import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq={}
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                freq[n]+=1
        for key,value in freq.items():
            if len(res)<k:
                heapq.heappush(res,[value,key])
            else:
                heapq.heappushpop(res,[value,key])
        return [key for value,key in res]



