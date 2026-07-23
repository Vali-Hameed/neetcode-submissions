class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            dupes = set()
            dupes.clear()
            for j in range(9):
                item = board[i][j]
                if item == '.':
                    continue
                elif int(item) not in dupes and int(item)<=9 and int(item)>=1:
                    dupes.add(int(item))
                    continue 
                else:
                    return False 
        for i in range(9):
            dupes.clear()
            for j in range(9):
                item = board[j][i]
                if item == '.':
                    continue
                elif int(item) not in dupes and int(item)<=9 and int(item)>=1:
                    dupes.add(int(item))
                    continue 
                else:
                    return False 
        
        for square in range(9):
            dupes.clear()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    item = board[row][col]
                    if item == '.':
                        continue
                    elif int(item) not in dupes and int(item)<=9 and int(item)>=1:
                        dupes.add(int(item))
                        continue 
                    else:
                        return False 

        
        return True


        