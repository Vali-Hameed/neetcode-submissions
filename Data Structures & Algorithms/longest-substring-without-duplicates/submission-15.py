class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupe={}
        L=0
        maxL=0
        count=0
        if len(s)==1:
            return 1

        for R in range(len(s)):
            if s[R] in dupe and dupe[s[R]]>=L:
                
                L=dupe[s[R]]+1
      
                
               
         
                
            length = (R-L)+1
            maxL=max(length,maxL)
                

            
            dupe.update({s[R]:R})

        return maxL
        