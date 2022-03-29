def get_winning_player(board):
    # Horizontal rown check
    for row in board:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != ".":
            print(f"Player {row[0]} is the Winner horizontal!")
            return row[0]
  
    # For vertical row check!= ["."]
    for col in range(len(board)):
        check = []

    for row in board:
        check.append(row[col])
        print("check", check)

        if check.count(check[0]) == len(check) and check[0] != ".":
            print(f"Player {check[0]} is the Winner vertical!")
            return check[0]

    # for diagonal row check
    diags = []
    for col, row in enumerate(reversed(range(len(board)))):
        diags.append(board[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != ".":
        print(f"Player {diags[0]} is the Winner diagonal!")
        return diags[0]

    diags = []
    for index in range(len(board)):
        diags.append(board[index][index])
    if diags.count(diags[0]) == len(diags) and diags[0] != ".":
        print(f"Player {diags[0]} is the Winner diagonal2!")
        return diags[0]

    return None


"""Should return the player that wins based on the tic tac toe rules.
If no player has won, than "None" is returned."""

  # to check if there is a winner

    


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_winning_player(board_1)) # should return "X"

  board_2 = [
    ["X", "O", "O"],
    ["X", "O", "."],
    ["O", "X", "X"],
  ]
  print(get_winning_player(board_2)) # should return "O"

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_winning_player(board_3)) # should return None