class Gomoku:
    def __init__(self):
        self.board_size = 15
        self.reset()

    def reset(self):
        self.board = [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def is_valid_move(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '.'

    def check_win(self, row, col):
        directions = [
            (1, 0), (0, 1), (1, 1), (1, -1)
        ]
        for dr, dc in directions:
            count = 1
            for delta in [-1, 1]:
                r, c = row + delta * dr, col + delta * dc
                while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == self.board[row][col]:
                    count += 1
                    r += delta * dr
                    c += delta * dc
            if count >= 5:
                return True
        return False
