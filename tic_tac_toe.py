from function0 import display_board
from function1 import get_menu_option
from function2 import get_empty_board
from function3 import get_human_coordinates
from function4 import get_random_ai_coordinates
from function5 import get_winning_player
from function6 import is_board_full


import itertools
import time
from colorama import Fore 
from colorama import Style


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3


def main():
    game_mode = get_menu_option(valid_input=False)
    board = get_empty_board()
    is_game_running = True
    while is_game_running:
        display_board(board)

        player_choice = itertools.cycle([f"{Fore.GREEN}{'X'}{Style.RESET_ALL}", f"{Fore.YELLOW}{'O'}{Style.RESET_ALL}"])
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
            
        if game_mode == 1:
            x, y = get_human_coordinates(board, current_player)
            display_board(x)
            winning_player = get_winning_player(board)
            if winning_player == "win":
                print("you are the winneeeer!!!!")
                display_board(x)
                exit()
            is_board_full(board)
            current_player = next(player_choice)
            print(f"Current Player: {current_player}")
            x, y = get_human_coordinates(board, current_player)
            
        elif game_mode == 2:
            x, y = get_random_ai_coordinates(board, current_player)
            time.sleep(1)
            display_board(x)
            winning_player = get_winning_player(board)
            if winning_player == "win":
                print("you are the winneeeer!!!!")
                display_board(x)
                exit()
            is_board_full(board)
            current_player = next(player_choice)
            print(f"Current Player: {current_player}")
            x, y = get_random_ai_coordinates(board, current_player)

        elif game_mode == 3:
            x, y = get_human_coordinates(board, current_player)
            display_board(x) 
            winning_player = get_winning_player(board)
            if winning_player == "win":
                print("you are the winneeeer!!!!")
                display_board(x)
                exit()
            is_board_full(board)
            current_player = next(player_choice)
            print(f"Current Player: {current_player}")
            x, y = get_random_ai_coordinates(board, current_player)
             
        winning_player = get_winning_player(board)
        is_board_full(board)


if __name__ == "__main__":
    main()