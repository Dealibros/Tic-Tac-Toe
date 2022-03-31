from colorama import Fore, Style

def is_board_full(board):
    for row in board:
        for item in row:
            if item == ".":
                return False
    print(f"{Fore.RED}{'Game Over. It is a Tie!'}{Style.RESET_ALL}\n")
    exit()
