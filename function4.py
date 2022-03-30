import random


def get_random_ai_coordinates(board, current_player): 
    while "." not in board:
        coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        a, b = random.choice(coordinates)
        if board[a][b] == ".":
            board[a][b] = current_player
            return board, current_player


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
      ["O", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print(get_random_ai_coordinates(board_1, "X"))