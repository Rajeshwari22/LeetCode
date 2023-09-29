class RandomizedSet:

    def __init__(self):
        self.rset=set()
        
    def insert(self, val: int) -> bool:
        if val in self.rset:
            return False
        else:
            self.rset.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        idx=random.randint(0,len(self.rset)-1)
        return list(self.rset)[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
