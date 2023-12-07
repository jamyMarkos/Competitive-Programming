class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        for row in range(len(board)):
            nums = [int(num) for num in board[row] if num.isdigit()]
            if len(set(nums)) < len(nums): 
                return False
            
        for col in range(len(board[0])):
            column = []
            for row in range(len(board)):
                if board[row][col].isdigit():
                    column.append(board[row][col])
            if len(set(column)) < len(column):
                return False
                

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                tmp = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l].isdigit():
                            if 1 <= int(board[k][l]) <= 9 and board[k][l] not in tmp:
                                tmp.append(board[k][l])
                            else:
                                return False
                        else:
                            continue
       
        return True
        