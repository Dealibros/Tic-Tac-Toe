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
   


  print(board)
  # The board is a list of lists.
  coordinates = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)] 
  a, b, c, d, e, f, g, h, i = coordinates
  print(a)
  # coordinates = [board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]]
  # choose_random_coordinate = random.choice(coordinates)
  choose_random_coordinate = coordinates.pop(random.randrange(len(coordinates)))
  # print(choose_random_coordinate.index(choose_random_coordinate))
  correct_format_coordinate = board[int(choose_random_coordinate[0]), int(choose_random_coordinate[1])]
  print("correct?", correct_format_coordinate)
  
  # pop will remove the chosen coordinate from the list
  # now the coordinate choosen by the other player must be remove as well
  
  print("coordinates left", coordinates)


  import random


def get_random_ai_coordinates(board, current_player):
    random_choose = True
    while random_choose:
        coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        randomcoord = coordinates.pop(random.randrange(len(coordinates)))
        print("randomcoord", randomcoord)
        a, b = randomcoord
        print(a, b)
        print("print new list", coordinates)
        if board[a][b] != "X" and board[a][b] != "O":
            random_choose = True
            return a, b
          
        else:
            random_choose = False
            print("This coordinate is already taken")
            

