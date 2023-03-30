class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for index,val in enumerate(nums):
            difference=target-val
            if difference in hashMap:
                return [hashMap[difference],index]
            hashMap[val]=index
