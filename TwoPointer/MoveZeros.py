class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lptr=0
        for rptr in range(len(nums)):
            if nums[rptr]:
                nums[lptr],nums[rptr]=nums[rptr],nums[lptr]
                lptr+=1
        return nums
