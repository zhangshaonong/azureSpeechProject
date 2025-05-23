def create_board(size):
    return [['-' for _ in range(size)] for _ in range(size)]


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def is_valid_move(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == '-'


def make_move(board, row, col, player):
    board[row][col] = player


def check_winner(board, player):
    size = len(board)
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for r in range(size):
        for c in range(size):
            if board[r][c] == player:
                for dr, dc in directions:
                    count = 0
                    for i in range(5):
                        nr, nc = r + dr * i, c + dc * i
                        if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == player:
                            count += 1
                        else:
                            break
                    if count == 5:
                        return True
    return False


def gomoku():
    size = 15
    board = create_board(size)
    players = ['X', 'O']
    current_player = 0
    
    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")
        
        try:
            row, col = map(int, input("Enter row and column (e.g., 7 7): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers.")
            continue
        
        if not is_valid_move(board, row, col):
            print("Invalid move. Try again.")
            continue

        make_move(board, row, col, players[current_player])

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    gomoku()
