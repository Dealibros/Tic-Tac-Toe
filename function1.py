def get_menu_option():
    game_mode = input("Choose your Game Mode\n1. Human vs Human\n2. Random AI vs Random AI\n3. Human vs Random AI\n4. Human vs Unbeatable AI\nYour choice is: ")
    if game_mode == 1:
        print("Your choice: Human vs Human")
        return 1
    elif game_mode == 2:
        print("Your choice: Random AI vs Random AI")
        return 2
    elif game_mode == 3:
        print("Human vs Random AI")
        return 3
    elif game_mode == 4:
        print("Human vs Unbeatable AI")
        return 4

  # There is a much shorter and elegant way to make this. Look it up
"""
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
 """ 

if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option) # if the user selected 1, it should print 1