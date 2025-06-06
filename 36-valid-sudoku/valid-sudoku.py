class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Prepare keys for dicts
                box_index = (r // 3, c // 3)
                
                # Initialize sets if not present
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box_index not in boxes:
                    boxes[box_index] = set()
                
                # Check if value already seen in row, col or box
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]):
                    return False
                
                # Mark value as seen
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
