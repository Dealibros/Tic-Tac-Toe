def get_human_coordinates(board, current_player):
  # needs to be corrected. 
    """ while(True):
      game_move = input("Your turn to move")
      row = ['A', 'B', 'C']
      column = [1, 2, 3]
      if row not in game_move or column not in game_move:
      elif len(game_move) != 2:
      elif game_move in game_already
        print("Wrong Input. Please try again")
      elif game_move === "Quit".low() or "Quit".upper()
      print("Game is over!")
      exit() """
    
    #N


 """Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop."""



if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones