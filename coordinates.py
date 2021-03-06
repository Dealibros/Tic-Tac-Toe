import random


def get_human_coordinates(board, current_player):
    guess = False
    while guess is False:
        answer = input("\nPlease enter the coordinates: ").upper()
        print(f"Your move is: {answer}\n")
        if answer == "QUIT":
            print("Game is over!")
            exit()
        elif answer[0] not in ["A", "B", "C"] or answer[1] not in ["1", "2", "3"]:
            print("Invalid input. Please try again.")
        elif answer:
            board_values = {'A1': board[0][0],
                            'A2': board[0][1],
                            'A3': board[0][2],
                            'B1': board[1][0],
                            'B2': board[1][1],
                            'B3': board[1][2],
                            'C1': board[2][0],
                            'C2': board[2][1],
                            'C3': board[2][2]}
            for values in board_values:
                if answer == values:
                    if board_values[values] == ".":
                        board[ord(answer[0]) - 65][int(answer[1]) - 1] = current_player
                        guess = True
                        return board, current_player
                    else:
                        print("This space is occupied. Please try again.")
                        break


def get_random_ai_coordinates(board, current_player): 
    while "." not in board:
        coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        a, b = random.choice(coordinates)
        if board[a][b] == ".":
            board[a][b] = current_player
            return board, current_player