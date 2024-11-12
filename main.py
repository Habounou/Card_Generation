import random

random_nbr = random.randint(0,100)

def art_print (text, align):
    art_result = "┌────────────────────────┐\n"
    if align == "l":
        for new_lines in range(0, 5):
            art_result += "│  " + text[new_lines] + " " * (20 - len(text[new_lines])) + "  │\n"
    elif align == "r":
        for new_lines in range(0, 5):
            art_result += "│  " + " " * (20 - len(text[new_lines])) + text[new_lines] + "  │\n"
    else:
        for new_lines in range(0, 5):
            if len(text[new_lines]) % 2 == 0:
                art_result += ("│  " + " " * ((20 - len(text[new_lines])) // 2) + text[new_lines] +
                               " " * ((20 - len(text[new_lines])) // 2) + "  │\n")
            else:
                art_result += ("│  \u202F\u200A" + " " * ((20 - len(text[new_lines])) // 2) + text[new_lines] +
                               " " * ((20 - len(text[new_lines])) // 2) + "\u202F  │\n")
    art_result += "└────────────────────────┘"
    return art_result

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

def card_print(art, effect):
    final_card = ["┌──────────────────────────────────────────────────┐",
                  "│ ████████████████████████████████████████████████ │",
                  "│ █                                              █ │",
                  "│ █               ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░               █ │",
                  "│ █           \u202F\u200A── DIGITAL DUEL CARD ──\u202F           █ │",
                  "│ █               ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░               █ │",
                  "│ █                                              █ │",
                  "│ ████████████████████████████████████████████████ │",
                  "├──────────────────────────────────────────────────┤",
                  "│        Card Name: ███████████████████████        │",
                  "│        Card Type: ████████                       │",
                  "│ ──────────────────────────────────────────────── │",
                  "│ █          " + art[0] + "          █ │",
                  "│ █          " + art[1] + "          █ │",
                  "│ █          " + art[2] + "          █ │",
                  "│ █          " + art[3] + "          █ │",
                  "│ █          " + art[4] + "          █ │",
                  "│ █          " + art[5] + "          █ │",
                  "│ █          " + art[6] + "          █ │",
                  "│ █                   [EFFECT]                   █ │",
                  "│ █   " + effect[0] + "   █ │",
                  "│ █   " + effect[1] + "   █ │",
                  "│ █   " + effect[2] + "   █ │",
                  "│ █   " + effect[3] + "   █ │",
                  "├──────────────────────────────────────────────────┤",
                  "│             ATK / RES: █████ / █████             │",
                  "└──────────────────────────────────────────────────┘"]
    return final_card

start_message = input("Welcome to the Digital Duel Card Creator. What are you here for?\n"
                      "→ To create a card (C)\n→ To browse your collection - Card_list.txt (B)\n")
if start_message.upper() == "C":
    while True:
        user_text = ["*********************"] * 5
        while len(user_text[0 and 1 and 2 and 3 and 4]) > 20:
            user_text[0] = input("Enter 5 lines of characters to create a new card (maximum 20 characters per line):\n"
                                 "           Maximum ↓\n")
            for lines in range (0, 4):
                user_text[lines + 1] = input("")
            if len(user_text[0 and 1 and 2 and 3 and 4]) > 20:
                print("You have exceeded the character limit in a line.")

        align_choice = "c"
        while True:
            print(art_print(user_text, align_choice))
            align_choice = input("Is the alignment right for you? (yes:Y/no:N)\n")
            if align_choice.upper() == "N":
                align_choice = input("Choose an alignment:\n→ Center (C)\n→ Left (L)\n→ Right (R)\n").lower()
            else:
                align_choice = "c"
                break

        art_list = art_print(user_text, align_choice).split("\n")

        card_effect = "This is an example."
        card_effect = effect_line_return(card_effect)

        print("\n".join(card_print(art_list, card_effect)))

        redo = input("Are you satisfied with this rendering? (yes:Y/no:N)\n").upper()
        if redo != "N":
            break

    with open("Card_list.txt", "a", encoding="utf-8") as txt_file:
        txt_file.write("│".join(user_text) + "│" + align_choice + "│")

    ascii_sum = 0
    for nbr_lines in range (0, 5):
        ascii_sum = sum(ord(char) for char in user_text[nbr_lines])
    random.seed(ascii_sum)

    print("Here is your card:")
    card_effect = effect_line_return(str(random.randint(0,10000000)))
    print("\n".join(card_print(art_list, card_effect)))

else:
    with open("Card_list.txt", "r", encoding="utf-8") as txt_file:
        card_list = txt_file.read().split("│")

    print("\u202F\u200A───────────────────────────────────────────────────────────────────────────"
          " CARD DATABASE ───────────────────────────────────────────────────────────────────────────\u202F\n")
    card_row = []
    for cards in range(0, 3):
        art_list = art_print(card_list[6 * cards: 6 * cards + 5], card_list[6 * cards + 6]).split("\n")
        card_effect = effect_line_return("test")
        card_row += card_print(art_list, card_effect)
    for card_height in range(0, len(card_row) // 3):
        print(card_row[card_height] + "     " + card_row[card_height + len(card_row) // 3] + "     " +
              card_row[card_height + 2 * len(card_row) // 3])
    user_action = input("→ To search a specific card (S)\n→ To see more result (Enter)\n→ To exit (Q)\n").upper()
    if user_action == "S":
        print()
    elif user_action == "":
        print()
    else:
        exit()