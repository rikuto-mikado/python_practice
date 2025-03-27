def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(b, p):
    return any([
        all([b[r][c] == p for c in range(3)]) for r in range(3)
    ]) or any([
        all([b[r][c] == p for r in range(3)]) for c in range(3)
    ]) or all([b[i][i] == p for i in range(3)]) or all([b[i][2-i] == p for i in range(3)])

board = [[" "]*3 for _ in range(3)]
turn = "X"

while True:
    print_board(board)
    print(f"{turn}'s turn")
    r = int(input("Row (0-2): "))
    c = int(input("Col (0-2): "))

    if board[r][c] != " ":
        print("Occupied! Try again.")
        continue

    board[r][c] = turn

    if check_win(board, turn):
        print_board(board)
        print(f"{turn} wins!")
        break

    if all(cell != " " for row in board for cell in row):
        print_board(board)
        print("Draw!")
        break

    turn = "O" if turn == "X" else "X"
