class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        lptr,rptr=0,len(nums)-1
        while lptr<rptr:
            nums[lptr],nums[rptr]=nums[rptr],nums[lptr]
            lptr+=1
            rptr-=1
        
        lptr,rptr=0,k-1
        while lptr<rptr:
            nums[lptr],nums[rptr]=nums[rptr],nums[lptr]
            lptr+=1
            rptr-=1

        lptr,rptr=k,len(nums)-1
        while lptr<rptr:
            nums[lptr],nums[rptr]=nums[rptr],nums[lptr]
            lptr+=1
            rptr-=1
