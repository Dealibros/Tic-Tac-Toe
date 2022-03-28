# Changed board for display Board


# def get_human_coordinates(display_board, player=0, row=0, column=0, just_display=False): Before
# The current player value is X or 0!!!
# board 
def get_human_coordinates(board, current_player): 

    A1 = board[0][0]
    A2 = board[0][1]
    A3 = board[0][2]
    B1 = board[1][0]
    B2 = board[1][1]
    B3 = board[1][2]
    C1 = board[2][0]
    C2 = board[2][1]
    C3 = board[2][2]

    """ board[0][0] = "A1"
    board[0][1] = "A2"
    board[0][2] = "A3"
    board[1][0] = "B1"
    board[1][1] = "B2"
    board[1][2] = "B3"
    board[2][0] = "C1"
    board[2][1] = "C2"
    board[2][2] = "C3" """

    guess = False
    while guess is False:
        answer = input("Please enter the coordinates: ")
        print("answer", answer)  # answer as input is always a string
        if answer == "quit".upper() or answer == "quit".lower():
            print("Game is over!")
            exit()
        elif answer[0] not in ["A", "B", "C"] or answer[1] not in ["1", "2", "3"]:
            print("Invalid input. Please try again.")
        elif answer == 'X' or answer == 'O':
            print("answer", answer)
            print("board", board)
            print("Invalid input. Please try again.")
            print("This space is occupied. Please try again.")
        else:
            guess = True
    return print(answer[0] + answer[1])

      
# get_human_coordinates(board, current_player)



"""  row = input("Choose your row from A-C: ")
column = input("Choose your column from 1-3: ") """

"""        # error1 "list indices must be integers or slices, not str"
            # error2 'list' object is not callable
        elif answer:
            # print("see answer"(answer[0] + answer[1]) # still a string
            print("board", board)
            # board value # board[['X', 'X', '.'], ['X', '.', '.'], ['X', 'X', '.']]
            # after the above line, board is a list of lists 
            # board[['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3']]
            # Maybe it could work through a dictionary? {A1: 'X', A2: 'X', A3: '.'}??


 """




""" Should return the read coordinates for the tic tac toe board from the terminal
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop. """

# Needs to be completly redone.
 
""" try:
column_choice = int(input("What column do you want to play? (1, 2, 3): "))
row_choice = input("What row do you want to play? (A, B, C): ")
      return print(column_choice, row_choice)
  if board_input == "Quit".lower() or "Quit".upper():
      print("Game is over!")
      exit()
  elif board_input[row][column] != 0:
      print("This position is taken! Choose another!")
      return  passdisplay_board, False
  if not just_display:
      display_board[row][column] = player
      return display_board, True

except IndexError as e:
  print("Error:make sure your input row/column as 0, 1, 2, A, B, C", e)
  return display_board, False

except Exception as e:
  print("Something went wrong!", e)
  return display_board, False

# From here move to end game !
while play:
  display_board()

game_won = False
game, _ = display_board(game, just_display=True)

# Selecting the player should be done on the end tic_tac_toe.py
player_choice = itertools.cycle([1, 2])
while not game_won:
  current_player = next(player_choice)
  print(f"Current Player: {current_player}")
  played = False

  while not played:
      column_choice = int(input("What column do you want to play? (1, 2, 3): "))
      row_choice = input("What row do you want to play? (A, B, C): ")
      return print(column_choice, row_choice)

  
# Should we ask for one input?  A?1? Or two? A1
  game, played = display_board(game, current_player, column_choice, row_choice)


# THis could be moved as well to the end code tic_tac_toe.py
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
      play = False """




if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones