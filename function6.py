def is_board_full(board):
    for row in board:
        for item in row:
            if item == ".":
                return False
    print("Game Over. It's a Tie!")
    exit()

    


if __name__ == "__main__":
    """  # run this file to test you have implemented correctly the function
      board_1 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
      ]
      print(is_board_full(board_1)) # should return False
"""