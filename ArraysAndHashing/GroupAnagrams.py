class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for word in strs:
            sortedWord="".join(sorted(word))
            if sortedWord not in dict:
                dict[sortedWord]=[word]
            else:
                dict[sortedWord].append(word)
        result=[]
        for item in dict.values():
            result.append(item)
        return result
