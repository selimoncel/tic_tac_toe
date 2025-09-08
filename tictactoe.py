import os

def print_board(board):
    print("\n   1   2   3")
    for i, row in enumerate(board):
        print(f"{i+1}  " + " │ ".join(row))
        if i < 2:
            print("  ───┼───┼───")
    print()

def get_move(player):
    while True:
        try:
            move = input(f"Player {player} - Enter your move (row col): ")
            row, col = map(int, move.strip().split())
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("❌ Invalid input. Please enter numbers between 1 and 3.")
                continue
            return row - 1, col - 1
        except ValueError:
            print("❌ Invalid format. Enter row and column numbers like: 2 3")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for _ in range(9):
        print_board(board)
        # Get valid move
        while True:
            row, col = get_move(current_player)
            if board[row][col] == " ":
                board[row][col] = current_player
                break
            else:
                print("❌ This cell is already taken. Try again.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            return
        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("🤝 Game over! It's a draw.")

def main():
    try:
        while True:
            play_game()
            choice = input("🔁 Play again? (y/n): ").strip().lower()
            if choice == "y":
                # ✅ clear the console
                os.system("clear" if os.name == "posix" else "cls")
                continue
            else:
                print("👋 Thanks for playing!")
                break
    except KeyboardInterrupt:
        print("\n👋 Exiting...")


if __name__ == "__main__":
    main()
