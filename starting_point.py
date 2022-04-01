from colorama import Fore, Back, Style

def banner():
    welcome_banner = [f"""

                                     _____  _  ____    _____  ____  ____    _____  ____  _____
                                    /__ __\/ \/   _\  /__ __\/  _ \/   _\  /__ __\/  _ \/  __/
                                      / \  | ||  /      / \  | / \||  /      / \  | / \||  \  
                                      | |  | ||  \__    | |  | |-|||  \__    | |  | \_/||  /_ 
                                      \_/  \_/\____/    \_/  \_/ \|\____/    \_/  \____/\____|
                                                            """]
    for i in welcome_banner:
        print(f"{Fore.CYAN}{i}{Style.RESET_ALL}")


def get_menu_option(valid_input):

    game = ["1. Human vs Human", "2. Random AI vs Random AI", "3. Human vs Random AI"]

    print("\nPICK YOUR GAME MODE\nChoose a number between 1 and 3:\n")
    print(f"{game[0]}\n{game[1]}\n{game[2]}\n")

    while valid_input is False:
        options = {"1": game[0][3:], "2": game[1][3:], "3": game[2][3:]}
        game_mode = input("Your choice is: ")
        for choice in options:
            if game_mode == choice: 
                print(f"\nGame Mode: {options[choice]}.\n")
                return int(game_mode)
        else:
            print("\nWrong input choice. Try again, by choosing a number between 1 and 3\n")

