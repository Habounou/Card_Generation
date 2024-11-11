import random

random_nbr = random.randint(0,100)

while True:
    user_text = ["*********************"] * 5
    while len(user_text[0 and 1 and 2 and 3 and 4]) > 20:
        user_text[0] = input("Enter 5 lines of characters to create a new card (maximum 20 characters per line):\n"
                             " ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓\n")
        for lines in range (0, 4):
            user_text[lines + 1] = input("").lower()
        if len(user_text[0 and 1 and 2 and 3 and 4]) > 20:
            print("You have exceeded the character limit in a line.")

    align_choice = "c"
    while True:
        art_result = "┌────────────────────────┐\n"
        if align_choice == "l":
            for new_lines in range(0, 5):
                art_result += "│  " + user_text[new_lines] + " " * (20 - len(user_text[new_lines])) + "  │\n"
        elif align_choice == "r":
            for new_lines in range(0, 5):
                art_result += "│  " + " " * (20 - len(user_text[new_lines])) + user_text[new_lines] + "  │\n"
        else:
            for new_lines in range(0, 5):
                if len(user_text[new_lines]) % 2 == 0:
                    art_result += ("│  " + " " * ((20 - len(user_text[new_lines])) // 2) + user_text[new_lines] +
                                   " " * ((20 - len(user_text[new_lines])) // 2) + "  │\n")
                else:
                    art_result += (
                            "│  \u202F\u200A" + " " * ((20 - len(user_text[new_lines])) // 2) + user_text[new_lines] +
                            " " * ((20 - len(user_text[new_lines])) // 2) + "\u202F  │\n")
        art_result += "└────────────────────────┘"
        print(art_result)
        align_choice = input("Is the alignment right for you? (yes:Y/no:N)\n")
        if align_choice.upper() == "N":
            align_choice = input("Choose an alignment:\n- center:C\n- left:L\n- right:R\n").lower()
        else:
            break

    art_result = art_result.split("\n")

    print("┌──────────────────────────────────────────────────┐\n"
          "│ ████████████████████████████████████████████████ │\n"
          "│ █                                              █ │\n"
          "│ █               ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░               █ │\n"
          "│ █           \u202F\u200A── DIGITAL DUEL CARD ──\u202F           █ │\n"
          "│ █               ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░               █ │\n"
          "│ █                                              █ │\n"
          "│ ████████████████████████████████████████████████ │\n"
          "├──────────────────────────────────────────────────┤\n"
          "│        Card Name: ███████████████████████        │\n"
          "│        Attribute: ████████                       │\n"
          "│ ──────────────────────────────────────────────── │\n"
          "│ █          " + art_result[0] + "          █ │\n"
          "│ █          " + art_result[1] + "          █ │\n"
          "│ █          " + art_result[2] + "          █ │\n"
          "│ █          " + art_result[3] + "          █ │\n"
          "│ █          " + art_result[4] + "          █ │\n"
          "│ █          " + art_result[5] + "          █ │\n"
          "│ █          " + art_result[6] + "          █ │\n"
          "│ █                   [EFFECT]                   █ │\n"
          "│ █   This is a                                  █ │\n"
          "│ █   Once per turn, you may discard 1 card to   █ │\n"
          "│ █   gain 300 ATK until the end of this turn.   █ │\n"
          "│ █                                              █ │\n"
          "├──────────────────────────────────────────────────┤\n"
          "│        ATK / DEF: █████ / █████                  │\n"
          "└──────────────────────────────────────────────────┘\n")

    redo = input("Are you satisfied with this rendering? (yes:Y/no:N)\n")
    if redo.upper() == "Y":
        break

ascii_sum = 0
for nbr_lines in range (0, 5):
    ascii_sum = sum(ord(char) for char in user_text[nbr_lines])
random.seed(ascii_sum)