class Solution:
    def isValid(self, s: str) -> bool:
        #use stack
        listOfPossibilities={")":"(","}":"{","]":"["}
        stack=[]
        for c in s:
            if c in listOfPossibilities:
                if stack and stack[-1]==listOfPossibilities[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
