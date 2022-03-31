from function0 import display_board
from function1 import get_menu_option
from function2 import get_empty_board
from function3 import get_human_coordinates
from function4 import get_random_ai_coordinates
from function5 import get_winning_player
from function6 import is_board_full
from banner import banner

import itertools
import time
from colorama import Fore, Style 


def main():
    banner()
    game_mode = get_menu_option(valid_input=False)
    board = get_empty_board()
    is_game_running = True
    while is_game_running:
        display_board(board)
        if game_mode == 2:
            time.sleep(1.5) 
            
        def finale():
            winning_player = get_winning_player(board)
            if winning_player == "win":
                print("\n.......WELL DONE.......")
                display_board(board)
                exit()
            else:
                is_board_full(board)
            
        def game_steps(first_player, second_player):
            player_choice = itertools.cycle([f"{Fore.GREEN}{'X'}{Style.RESET_ALL}", f"{Fore.YELLOW}{'O'}{Style.RESET_ALL}"])

            current_player = next(player_choice)
            print(f"Current Player: {current_player}")
            first_player(board,current_player)

            display_board(board)
            if game_mode == 2:
                time.sleep(1.5) 
            finale()

            current_player = next(player_choice)
            print(f"Current Player: {current_player}")
            second_player(board,current_player)
            finale()
            return board

        if game_mode == 1:
            board = game_steps(get_human_coordinates, get_human_coordinates)
        elif game_mode == 2:
            board = game_steps(get_random_ai_coordinates, get_random_ai_coordinates)
        elif game_mode == 3:
            board = game_steps(get_human_coordinates, get_random_ai_coordinates)
            

if __name__ == "__main__":
    main()