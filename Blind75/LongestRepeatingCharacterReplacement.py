class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countS={}
        res=0
        l=0
        for r in range(len(s)):
            countS[s[r]]=1+countS.get(s[r],0)
            while (r-l+1)-max(countS.values())>k:
                countS[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
