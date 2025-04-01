class Gomoku:
    def __init__(self):
        self.board_size = 15
        self.board = [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'

    def print_board(self):
        print('  ' + ' '.join(str(i) for i in range(self.board_size)))
        for i, row in enumerate(self.board):
            print(f'{i} ' + ' '.join(row))

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
                while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == self.current_player:
                    count += 1
                    r += delta * dr
                    c += delta * dc
            if count >= 5:
                return True
        return False

    def play(self):
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")
            try:
                row, col = map(int, input("Enter row and column (e.g., '7 7'): ").split())
                if not self.is_valid_move(row, col):
                    print("Invalid move! Try again.")
                    continue

                self.board[row][col] = self.current_player
                if self.check_win(row, col):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break

                self.current_player = 'O' if self.current_player == 'X' else 'X'
            except ValueError:
                print("Please enter two numbers separated by a space.")
