def display_board(board):

    line = "   ---+---+---"

    print(f"""\n        1   2   3\n
    A   {board[0][0]} | {board[0][1]} | {board[0][2]}\n    {line}
    B   {board[1][0]} | {board[1][1]} | {board[1][2]}\n    {line}
    C   {board[2][0]} | {board[2][1]} | {board[2][2]}\n    {line}\n""")
