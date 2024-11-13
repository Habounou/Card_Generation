import random

random_nbr = random.randint(0,100)

def card_search(card_list_ref, s_criteria):
    s_results = []
    for cards in range(0, (len(card_list_ref) - 1) // 6):
        for elements in range(0, 5):
            if s_criteria in card_list_ref[6 * cards + elements]:
                s_results += card_list_ref[6 * cards: 6 * cards + 6]
    if s_results:
        s_results += [""]
    return s_results

def row_print(card_list_ref, effect, page = 0):
    card_row = []
    row_print_result = ""
    for cards in range(0 + page * 3, 3 + page * 3):
        if (len(card_list_ref[page * 18:]) - 1) / 6 >= (cards - page * 3) + 1:
            art_in_row = art_print(card_list_ref[6 * cards: 6 * cards + 5], card_list_ref[6 * cards + 5]).split("\n")
            card_effect_in_row = effect_line_return(effect)
            card_row += card_print(art_in_row, card_effect_in_row)
    for card_height in range(0, 27):
        if (len(card_list_ref[page * 18:]) - 1) / 6 >= 3:
            row_print_result += (card_row[card_height] + "     " + card_row[card_height + 27] + "     " +
                                 card_row[card_height + 54] + "\n")
        elif (len(card_list_ref[page * 18:]) - 1) / 6 == 2:
            row_print_result += (card_row[card_height] + "     " +
                                 card_row[card_height + 27] + "\n")
        elif (len(card_list_ref[page * 18:]) - 1) / 6 == 1:
            row_print_result += (card_row[card_height] + "\n")
        else:
            return "No more cards in your collection could be found."
    return row_print_result

def art_print(text, align):
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
                if len(spaced_effect[rows]) + len(effect[current_index]) + 1 <= 40:
                    spaced_effect[rows] += effect[current_index] + " "
                    current_index += 1
                elif len(spaced_effect[rows]) + len(effect[current_index]) <= 40:
                    spaced_effect[rows] += effect[current_index]
                    current_index += 1
                else:
                    break
            else:
                spaced_effect[rows] += " " * (40 - len(spaced_effect[rows]))
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
            modify_align = input("Is the alignment right for you? (yes:Y/no:N)\n")
            if modify_align.upper() == "N":
                align_choice = input("Choose an alignment:\n→ Center (C)\n→ Left (L)\n→ Right (R)\n").lower()
            else:
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
    card_effect = effect_line_return(str(random.randint(0,10000000)) + " This is a test")
    print("\n".join(card_print(art_list, card_effect)))

else:
    with open("Card_list.txt", "r", encoding="utf-8") as txt_file:
        card_list = txt_file.read().split("│")

    print("───────────────────────────────────────────────────────────────────────────\u202F CARD\u200A"
          " DATABASE \u202F───────────────────────────────────────────────────────────────────────────\n")
    page_index = 0
    print(row_print(card_list, "test"))
    while True:
        user_action = input("→ To search a specific card (S)\n→ To see more result (Enter)\n→ To exit (Q)\n").upper()
        if user_action == "S":
            while True:
                search_criteria = input("You are searching for:\n")
                new_card_list = card_search(card_list, search_criteria)
                print(row_print(new_card_list, "test"))
                user_action = input("→ To search for another card (S)"
                                    "\n→ To see more result (Enter)\n→ To exit to the main menu (Q)\n").upper()
                if user_action == "S":
                    continue
                elif user_action == "":
                    page_index += 1
                    print(row_print(new_card_list, "test", page_index))
                else:
                    page_index = 0
                    break
        elif user_action == "":
            page_index += 1
            print(row_print(card_list, "test", page_index))
        else:
            break