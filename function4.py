import random




def get_random_ai_coordinates(board, current_player):
    random_choice = True
    while random_choice: 
        coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        a, b = coordinates.pop(random.randrange(len(coordinates)))
        print(a, b)
        if board[a][b] != "X" and board[a][b] != "O":
            board[a][b] = current_player
            random_choice = True
            return board[a][b]   
        else:
            random_choice = False
            print(a, b)
            print("cydd")
            break


    """
    Should return a tuple of 2 numbers. 
    Each number should be between 0-2. 
    The chosen number should be only a free coordinate from the board.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """

    """def get_coord():
        return (1, 1)


    ai_move = get_coord()
    board[ai_move[0]][ai_move[1]] = 'X'
    print(board)

    x_coord, y_coord = get_coord()
    board[x_coord][y_coord] = 'O'
    print(board)"""

     
      #board[choose_random_coordinate[0],choose_random_coordinate[1]] = current_player
      



if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
  """ print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
  print(get_random_ai_coordinates(board_1, "X")) # the printed coordinate should be only (0,2) or (1,2)
 """
  
  """ board_2 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print(get_random_ai_coordinates(board_2, "O")) """ # the printed coordinate should be None