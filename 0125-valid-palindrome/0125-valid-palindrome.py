class Solution:
    def isAlpha(self,s,i):
        x=ord(s[i])
        if 48<=x<=57 or 97<=x<=122:
            return True
        else:
            return False
                    
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        i,j=0,n-1
        s=s.lower()
        while i<j:
            if not self.isAlpha(s,i):
                i+=1
                continue
            if not self.isAlpha(s,j):
                j-=1
                continue
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                 return False
        return True
    

        