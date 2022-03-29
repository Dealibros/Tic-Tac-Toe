# Changed board for display Board


# def get_human_coordinates(display_board, player=0, row=0, column=0, just_display=False): Before
# The current player value is X or 0!!!
# board 
def get_human_coordinates(board, current_player): 

  
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
        answer = input("Please enter the coordinates: ").upper()
        print("answer", answer)  # answer as input is always a string
        if answer == "QUIT":
            print("Game is over!")
            exit()
        elif answer[0] not in ["A", "B", "C"] or answer[1] not in ["1", "2", "3"]:
            print("Invalid input. Please try again.")
           
        elif answer:
            board_values = {'A1': board[0][0], 'A2': board[0][1], 'A3': board[0][2], 'B1': board[1][0], 'B2': board[1][1],  'B3': board[1][2], 'C1': board[2][0], 'C2': board[2][1], 'C3': board[2][2]}
            for values in board_values:
                # print(values, board_values[values])
                if answer == values:
                    if board_values[values] == ".":
                        board[ord(answer[0]) - 65][int(answer[1]) - 1] = current_player
                        guess = True
                        return board, current_player
                    else:
                        print("This space is occupied. Please try again.")
                        break

      
# get_human_coordinates(board, current_player)




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
 



""" # THis could be moved as well to the end code tic_tac_toe.py
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
# coordinates = get_human_coordinates(board_1, "X")
# print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones