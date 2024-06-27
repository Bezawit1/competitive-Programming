class Solution(object):
    def updateBoard(self, board, click):
        def count_mines(board, row, col):
            mines_count = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            
            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'M':
                    mines_count += 1
                    
            return mines_count

        def dfs(row, col):
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] != 'E':
                return
            
            mines = count_mines(board, row, col)
            if mines == 0:
                board[row][col] = 'B'
                for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    dfs(row + d_row, col + d_col)
            else:
                board[row][col] = str(mines)

        click_row, click_col = click
        if board[click_row][click_col] == 'M':
            board[click_row][click_col] = 'X'
        else:
            dfs(click_row, click_col)

        return board
