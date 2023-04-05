class Solution:
    def isValid(self, s: str) -> bool:
        #use stack
        stack=[]
        listOfPossibilties={')':'(','}':'{',']':'['}
        for c in s:
            if c in listOfPossibilties:
                if stack and stack[-1]==listOfPossibilties[c]:
                    stack.pop()
                else:
                    return False
            stack.append(c)
        return stack if True else False
