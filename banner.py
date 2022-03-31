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