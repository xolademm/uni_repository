def game_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        game_board(board)
        print(f"Player {current_player}'s turn")

        # Get the player's move
        row = int(input("Enter your row (0, 1, or 2): "))
        col = int(input("Enter your column (0, 1, or 2): "))

        if row > 2:
            print("row out of range")
            
        if col > 2:
            print("column out of range")
            break

        # Check if the move is valid
        if board[row][col] != ' ':
            print("This spot has been marked. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner or a draw
        if check_winner(board, current_player):
            game_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            game_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
