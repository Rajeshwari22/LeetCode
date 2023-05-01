class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countofText=Counter(text)
        countOfBalloon=Counter("balloon")
        res=len(text)
        for c in countOfBalloon:
            res=min(res,countofText[c]//countOfBalloon[c])
        return res
