def get_menu_option(valid_input):

    g1 = "1. Human vs Human"
    g2 = "2. Random AI vs Random AI"
    g3 = "3. Human vs Random AI"

    print("\nPick your game mode(Choose a number between 1 and 3):\n")

    print(f"{g1}\n{g2}\n{g3}\n")

    while valid_input is True:
        game_mode = input("Your choice: ")
        if game_mode == "1":
            print(f"\nYou choose: {g1[3:]}.\nLet's play number:")
            return 1
        elif game_mode == "2":
            print(f"\nYou choose: {g2[3:]}.\nLet's play number:")
            return 2
        elif game_mode == "3":
            print(f"\nYou choose: {g3[3:]}.\nLet's play number:")
            return 3
        else:
            if not valid_input:
                print("\nWrong input choice. Try again, by choosing a number between 1 and 4\n")
      

if __name__ == "__main__":
    option = get_menu_option(valid_input=False)
    print(option)

