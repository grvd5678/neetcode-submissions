from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = board[r][c]
                square_key = (r // 3, c // 3)
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_key]):
                    return False
                
                cols[c].add(val)
                rows[r].add(val)
                squares[square_key].add(val)
        return True
        