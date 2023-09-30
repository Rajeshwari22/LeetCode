class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        if grid==[[0]]:
            return 1
        q=[(0,0,1)]
        grid[0][0]=1
        while q:
            x,y,length=q.pop(0)
            for x1 in [x-1,x,x+1]:
                for y1 in [y-1,y,y+1]:
                    if x1==len(grid)-1 and y1==len(grid[0])-1:
                        return length+1
                    if x1>=0 and x1<len(grid) and y1>=0 and y1<len(grid[0]):
                        if grid[x1][y1]==0:
                            q.append((x1,y1,length+1))
                            grid[x1][y1]=1
        return -1
