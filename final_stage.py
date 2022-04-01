from colorama import Fore, Style


def check_row(orientation):
    if orientation.count(orientation[0]) == len(orientation) and orientation[0] != "." and len(orientation) == 3:
        print(f"{Fore.MAGENTA}{'PLAYER '}{Style.RESET_ALL}{orientation[0]}{Fore.MAGENTA}{' IS THE WINNER!'}{Style.RESET_ALL}")
        return True
   

def get_winning_player(board):
    # Horizontal rown check 
    for row in board:
        if check_row(row):
            return "win"
  
    # For vertical row check!
    
    for col in range(len(board)):
        pillar = []
        for row in board:
            pillar.append(row[col])
            if check_row(pillar):
                return "win"

    # for diagonal row check
    diags_left = []
    for col, row in enumerate(reversed(range(len(board)))):
        diags_left.append(board[row][col])
    if check_row(diags_left):
        return "win"
       
    diags_right = []
    for index in range(len(board)):
        diags_right.append(board[index][index])
    if check_row(diags_right):
        return "win"


def is_board_full(board):
    for row in board:
        for item in row:
            if item == ".":
                return False
    print(f"{Fore.RED}{'Game Over. It is a Tie!'}{Style.RESET_ALL}\n")
    exit()
