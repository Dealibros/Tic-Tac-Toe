import itertools

# Changed board for display Board
def get_human_coordinates(display_board, player=0, row=0, column=0, just_display=False): 
  try:
    if display_board == "Quit".lower() or "Quit".upper():
      print("Game is over!")
      exit()
    elif display_board[row][column] != 0:
        print("This position is taken! Choose another!")
        return display_board, False
    if not just_display:
        display_board[row][column] = player
        return display_board, True

  except IndexError as e:
    print("Error:make sure your input row/column as 0, 1, 2, A, B, C", e)
    return display_board, False

  except Exception as e:
    print("Something went wrong!", e)
    return display_board, False


  play = True
  players = [1,2]
  while play:
    display_board()

    game_won = False
    game, _ = display_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
      current_player = next(player_choice)
      print(f"Current Player: {current_player}")
      played = False

      while not played:
        column_choice = int(input("What column do you want to play? (1, 2, 3): "))
        row_choice = input("What row do you want to play? (A, B, C): ")
        # Should we ask for one input?  A?1? Or two? A1
        game, played = display_board(game, current_player, column_choice, row_choice)
    

    if get_human_coordinates(game):
      game_won = True
      again = input("The game is over, would you like to play again? (y/n) ")
      if again.lower() == "y":
          print("restarting")
      elif again.lower() == "n":
        print("Bye")
        play = False
      else:
        print("Not a valid answer")
      play = False


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