class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #first row is just 1
        res=[[1]]
        #numRows-1 cause 1st row is already constructed
        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
            #append 0's front and the end
            
            #construct a new row
            
            #new row would have one item more than prev
            
                #add two values
                
