class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for s in strs:
            sortedword="".join(sorted(s))
            if sortedword not in dict:
                dict[sortedword]=[s]
            else:
                dict[sortedword].append(s)
        res=[]
        for i in dict.values():
            res.append(i)
        return res

        
