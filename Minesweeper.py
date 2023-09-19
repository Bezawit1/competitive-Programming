class Solution(object):
    def updateBoard(self, board, click):
        def count_mines(board, r, c):
            mines = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'M':
                    mines += 1
                    
            return mines
        
        def dfs(r, c):
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or board[r][c] != 'E':
                return
            
            mines = count_mines(board, r, c)
            if mines == 0:
                board[r][c] = 'B'
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    dfs(r + dr, c + dc)
            else:
                board[r][c] = str(mines)
        
        click_r, click_c = click
        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
        else:
            dfs(click_r, click_c)
        
        return board
