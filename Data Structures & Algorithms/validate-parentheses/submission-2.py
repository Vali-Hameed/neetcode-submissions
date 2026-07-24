class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(','{','[']
        closed = [')','}',']']

        characters = []

        for i in range(len(s)):
            if s[i] in open:
                characters.append(s[i])
            if s[i] in closed:
                index = closed.index(s[i])
                if len(characters) == 0:
                    return False
                if characters[-1] != open[index]:
                    return False
                else:
                    characters.pop()

        if len(characters)<1:
            return True
        else:
            return False 

# if bracket is closing then the top of the stack has to be the correct opening type