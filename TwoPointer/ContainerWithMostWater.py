class Solution:
    def isPalindrome(self, s: str) -> bool:
        lptr,rptr=0,len(s)-1
        while lptr<rptr:
            while lptr<rptr and not self.alphanum(s[lptr]):
                lptr+=1
            while rptr>lptr and not self.alphanum(s[rptr]):
                rptr-=1
            if s[lptr].lower()!=s[rptr].lower():
                return False
            lptr+=1
            rptr-=1
        return True
    
    def alphanum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or
        ord('a')<=ord(c)<=ord('z')or
        ord('0')<=ord(c)<=ord('9'))


         
         
         
         
         
         


