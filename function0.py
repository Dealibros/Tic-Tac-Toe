def display_board(board):
  #"""
  #Should print the tic tac toe board in a format similar to
     #  1   2   3
   # A   X | O | . 
    #   ---+---+---
    #B   X | O | .
     #  --+---+---
   # C   0 | X | . 
    #   --+---+---
  #"""
   board = [
      ['.', ".", "."],
      ['.', ".", "."],
      ['.', ".", "."]
   ]
   
   line = "   ---+---+---"
   
   print("\n    1   2   3\n")
   print(f"A   {board[0][0]} | {board[0][2]} | {board[0][2]}")
   print(line)
   print(f"B   {board[1][0]} | {board[1][2]} | {board[1][2]}")
   print(line)
   print(f"C   {board[2][0]} | {board[2][2]} | {board[2][2]}")
   print(line, "\n")



if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."]
    ]
    display_board(board)
    # should print 
    #     1   2   3
    # A   X | O | . 
    #    ---+---+---
    # B   X | O | .
    #    --+---+---
    # C   0 | X | . 
    #    --+---+---