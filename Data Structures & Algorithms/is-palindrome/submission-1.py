class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        ostring=""
        valid="abcdefghijklmnopqrstuvwxyz0123456789"
        s=s.lower()
        for i in range(len(s)-1,-1,-1):
            if  s[i] in valid: 
                string+=s[i]
        for i in range(len(s)):
            if  s[i] in valid: 
                ostring+=s[i]

        
        
       

        
        if ostring == string:
            return True
        else:
            return False
        