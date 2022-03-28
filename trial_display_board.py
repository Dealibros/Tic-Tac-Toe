from function2 import get_empty_board


def display_board(board):
  board = get_empty_board(board)
  for row in board:
    return print(row)

  line = "   ---+---+---"
  
    print("\n    1   2   3\n")
    print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(line)
    print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(line)
    print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print(line, "\n")


"""board = [
      ['.', ".", "."],
      ['.', ".", "."],
      ['.', ".", "."]
   ] """
   
