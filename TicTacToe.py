field_easy = ["",
              "1", "2", "3",
              "4", "5", "6",
              "7", "8", "9"]

active_player = "X"
run = True


def print_field():
    print(field_easy[1] + "|" + field_easy[2] + "|" + field_easy[3])
    print(field_easy[4] + "|" + field_easy[5] + "|" + field_easy[6])
    print(field_easy[7] + "|" + field_easy[8] + "|" + field_easy[9])


def game_move():
    global run
    while True:
        player_move = input("Enter your field: ").upper()
        if player_move == "QUIT" or player_move == "Q":
            run = False
            return
        player_move = int(player_move)
        if 1 <= player_move <= 9:
            if field_easy[player_move] == "X" or field_easy[player_move] == "O":
                print("This field is already occupied. Please choose a free field.")
            else:
                return player_move
        else:
            print("Invalid Entry, please try again!")


def change_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"


def win_check():
    # Check Zeilen
    if field_easy[1] == field_easy[2] == field_easy[3]:
        return field_easy[1]
    if field_easy[4] == field_easy[5] == field_easy[6]:
        return field_easy[4]
    if field_easy[7] == field_easy[8] == field_easy[9]:
        return field_easy[7]
    # Check Spalten
    if field_easy[1] == field_easy[4] == field_easy[7]:
        return field_easy[1]
    if field_easy[2] == field_easy[5] == field_easy[8]:
        return field_easy[2]
    if field_easy[3] == field_easy[6] == field_easy[9]:
        return field_easy[3]
    # Check Diagonal
    if field_easy[1] == field_easy[5] == field_easy[9]:
        return field_easy[1]
    if field_easy[3] == field_easy[5] == field_easy[7]:
        return field_easy[3]


def draw_check():
    if field_easy[1] != "1" and field_easy[2] != "2" and field_easy[3] != "3" and field_easy[4] != "4" \
            and field_easy[5] != "5" and field_easy[6] != "6" and field_easy[7] != "7" \
            and field_easy[8] != "8" and field_easy[9] != "9":
        return True


while run:
    print_field()
    next_move = game_move()
    if next_move is not None:
        field_easy[next_move] = active_player
        winner = win_check()
        if winner:
            print(f"Spieler {winner} hat gewonnen!")
            run = False
        if draw_check():
            print("Unentschieden")
            run = False
        change_player()