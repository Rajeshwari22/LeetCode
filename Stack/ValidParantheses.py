class Solution:
    def isValid(self, s: str) -> bool:
        #use stack
        stack=[]
        listOfPossibilties={")":"(","}":'{',"]":"["}
        for c in s:
            if c in listOfPossibilties:
                if stack and stack[-1]==listOfPossibilties[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
