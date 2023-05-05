class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed=False
        for i in range(len(nums)-1):
            if nums[i+1]>=nums[i]:
                continue
            if changed:
                return False
            # we want to decrease the left element
            #[3,4,2]
            #[i-1,i,i+1]
            if i==0 or nums[i+1]>=nums[i-1]:
                nums[i]=nums[i+1]
            #[4,2]
            else:
                nums[i+1]=nums[i]
            changed=True
        return True
