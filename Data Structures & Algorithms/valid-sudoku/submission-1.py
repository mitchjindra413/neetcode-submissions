class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == ".":
                    continue
                grid = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in grids[grid]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                grids[grid].add(val)
        
        return True
