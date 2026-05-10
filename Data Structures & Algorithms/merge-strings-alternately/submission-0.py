class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<len(word2):
            length = len(word1)
        else:
            length = len(word2)

        string=''
        for i in range(length):
            string+=word1[i]
            string+=(word2[i])
            count=i
        string+=(word1[count+1:])
        string+=(word2[count+1:])
        return string

        