class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        output=collections.defaultdict(list)

        def findTheDiff(word):
            if len(word)>1:
                lst=[]
                for x in range(len(word)-1):
                    diff=ord(word[x])-ord(word[x+1])
                    if diff<0:
                        diff=diff+26
                    lst.append(diff)
                return tuple(lst)

        for word in strings:
            output[findTheDiff(word)].append(word)
        return[output[x] for x in output]
        
