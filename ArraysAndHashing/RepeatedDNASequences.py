class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        res=set()
        for l in range(len(s)-9):
            curr=s[l:l+10]
            if curr in seen:
                res.add(curr)
            seen.add(curr)
        return list(res)
