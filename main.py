import random

random_nbr = random.randint(0,100)

while True:
    user_text = ["*********************"] * 5
    while len(user_text[0 and 1 and 2 and 3 and 4]) > 20:
        user_text[0] = input("Enter 5 lines of characters to create a new card (maximum 20 characters per line):\n"
                             "           Maximum ↓\n")
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
            align_choice = input("Choose an alignment:\n→ Center (C)\n→ Left (L)\n→ Right (R)\n").lower()
        else:
            break

    art_result = art_result.split("\n")

    def effect_line_return(effect):
        spaced_effect = ["", "", "", ""]
        effect = effect.split()
        current_index = 0
        for rows in range(0, 4):
            while len(spaced_effect[rows]) < 40:
                if current_index < len(effect):
                    if len(spaced_effect[rows]) + len(effect[current_index]) < 40:
                        spaced_effect[rows] += effect[current_index]
                        current_index += 1
                        if current_index != len(effect) - 1:
                            spaced_effect[rows] += " "
                    else:
                        spaced_effect[rows] += " "
                else:
                    spaced_effect[rows] += " "
        return spaced_effect

    card_effect = "This is an example."
    card_effect = effect_line_return(card_effect)

    def card_print(art, effect):
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
              "│        Card Type: ████████                       │\n"
              "│ ──────────────────────────────────────────────── │\n"
              "│ █          " + art[0] + "          █ │\n"
              "│ █          " + art[1] + "          █ │\n"
              "│ █          " + art[2] + "          █ │\n"
              "│ █          " + art[3] + "          █ │\n"
              "│ █          " + art[4] + "          █ │\n"
              "│ █          " + art[5] + "          █ │\n"
              "│ █          " + art[6] + "          █ │\n"
              "│ █                   [EFFECT]                   █ │\n"
              "│ █   " + effect[0] + "   █ │\n"
              "│ █   " + effect[1] + "   █ │\n"
              "│ █   " + effect[2] + "   █ │\n"
              "│ █   " + effect[3] + "   █ │\n"
              "├──────────────────────────────────────────────────┤\n"
              "│             ATK / RES: █████ / █████             │\n"
              "└──────────────────────────────────────────────────┘\n")

    card_print(art_result, card_effect)

    redo = input("Are you satisfied with this rendering? (yes:Y/no:N)\n")
    if redo.upper() == "Y":
        break

ascii_sum = 0
for nbr_lines in range (0, 5):
    ascii_sum = sum(ord(char) for char in user_text[nbr_lines])
random.seed(ascii_sum)