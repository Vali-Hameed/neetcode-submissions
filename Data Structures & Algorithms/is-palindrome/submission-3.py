class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeriacl="abcdefghijklmnopqrstuvwxyz0123456789"
        
        left =0
        s=s.lower()
        ss=[]
        for i in range(len(s)):
            if s[i] in alphanumeriacl:
                ss.append(s[i])
        right = len(ss)-1
        while left<=right:
            if ss[left]!=ss[right]:
                return False

            left+=1
            right-=1


        return True            
