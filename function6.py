def is_board_full(board):
    for row in board:
        for item in row:
            if item == ".":
                return False
    print("Game Over. It's a Tie!")
    exit()
