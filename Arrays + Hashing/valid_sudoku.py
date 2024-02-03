class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """    
        def has_duplicates(list):
            # Utility function to check if there are any duplicates in a given list
            seen = set()
            for num in list:
                if num != "." and num in seen:
                    return True
                seen.add(num)
            return False

        def check_row(row):
            # Check the given row for duplicates
            return not has_duplicates(board[row])
    
        def check_column(col):
            # Check the given column for duplicates
            column = [board[i][col] for i in range(9)]
            return not has_duplicates(column)

        def check_grid(row, col):
            # Turn the 3x3 subgrid into a single list and check for duplicates
            subgrid = [board[i][j] for i in range(row, row+3) for j in range(col, col+3)]
            return not has_duplicates(subgrid)
        
        for i in range(9):
            if not check_row(i) or not check_column(i):
                # If there are duplicates in any row or column, return False
                return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_grid(i,j):
                    # If there are duplicates in any 3x3 subgrid, return False
                    return False
        

        return True

           
                
        
if __name__ == "__main__":
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol.isValidSudoku(board)