class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        lptr,rptr=0,len(height)-1
        while lptr<rptr:
            area=(rptr-lptr)*min(height[lptr],height[rptr])
            res=max(area,res)
            if height[lptr]<height[rptr]:
                lptr+=1
            elif height[rptr]<height[lptr]:
                rptr-=1
            else:
                rptr-=1
        return res
