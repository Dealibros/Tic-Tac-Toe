def display_board(board):

    line = "   ---+---+---"

    print("\n    1   2   3\n")
    print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(line)
    print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(line)
    print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print(line, "\n")


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."]
    ]
    display_board(board)