import random
from game_effects import create_effect

def row_completion_l(text):
    complete_row_l = text + " " * (48 - len(text))
    return complete_row_l

def row_completion_c(text, length = 48):
    complete_row_c = ""
    if len(text) % 2 != 0:
        complete_row_c = " "
    complete_row_c += " " * ((length - len(text)) // 2) + text + " " * ((length - len(text)) // 2)
    return complete_row_c

def card_search(card_list_ref, s_criteria = None, s_min = 0, s_max = 5, type_criteria = None):
    s_results = []
    operator = "or"
    if s_criteria and type_criteria:
        operator = "and"
    for cards in range(0, (len(card_list_ref) - 1) // 9):
        for elements in range(s_min, s_max):
            if s_min == 8 and s_max == 9 and s_criteria in create_effect(card_list_ref[9 * cards + 8],
                                                                         card_list_ref[9 * cards + 7]):
                s_results += card_list_ref[9 * cards: 9 * cards + 9]
                break
            else:
                if operator == "or":
                    if s_criteria:
                        if s_criteria in card_list_ref[9 * cards + elements]:
                            s_results += card_list_ref[9 * cards: 9 * cards + 9]
                            break
                    if type_criteria:
                        if type_criteria in card_list_ref[9 * cards + 7]:
                            s_results += card_list_ref[9 * cards: 9 * cards + 9]
                            break
                if operator == "and":
                    if (s_criteria in card_list_ref[9 * cards + elements] and
                            type_criteria in card_list_ref[9 * cards + 7]):
                        s_results += card_list_ref[9 * cards: 9 * cards + 9]
                        break
    if s_results:
        s_results += [""]
    return s_results

def row_print(card_list_ref, page = 0):
    card_row = []
    row_print_result = ""
    for cards in range(0 + page * 3, 3 + page * 3):
        if (len(card_list_ref[page * 27:]) - 1) / 9 >= (cards - page * 3) + 1:
            art_in_row = art_print(card_list_ref[9 * cards: 9 * cards + 5], card_list_ref[9 * cards + 5]).split("\n")
            card_effect_in_row = effect_line_return(create_effect(card_list_ref[9 * cards + 8],
                                                                  card_list_ref[9 * cards + 7]))
            card_row += card_print(art_in_row, card_effect_in_row, row_completion_l(card_list_ref[9 * cards + 6]),
                                   row_completion_c(card_list_ref[9 * cards + 7]),
                                   row_completion_c(card_list_ref[9 * cards + 8], 44))
    for card_height in range(0, 31):
        if (len(card_list_ref[page * 27:]) - 1) / 9 >= 3:
            row_print_result += (card_row[card_height] + card_row[card_height + 31] +
                                 card_row[card_height + 62] + "\n")
        elif (len(card_list_ref[page * 27:]) - 1) / 9 == 2:
            row_print_result += (card_row[card_height] +
                                 card_row[card_height + 31] + "\n")
        elif (len(card_list_ref[page * 27:]) - 1) / 9 == 1:
            row_print_result += (card_row[card_height] + "\n")
        else:
            return "No cards in your collection could be found."
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
                art_result += ("│   " + " " * ((20 - len(text[new_lines])) // 2) + text[new_lines] +
                               " " * ((20 - len(text[new_lines])) // 2) + "  │\n")
    art_result += "└────────────────────────┘"
    return art_result

def effect_line_return(effect):
    spaced_effect = ["", "", "", "", "", ""]
    effect = effect.split()
    current_index = 0
    for rows in range(0, 6):
        while len(spaced_effect[rows]) < 42:
            if current_index < len(effect):
                if len(spaced_effect[rows]) + len(effect[current_index]) + 1 <= 42:
                    spaced_effect[rows] += effect[current_index] + " "
                    current_index += 1
                elif len(spaced_effect[rows]) + len(effect[current_index]) <= 42:
                    spaced_effect[rows] += effect[current_index]
                    current_index += 1
                else:
                    break
            else:
                break
        spaced_effect[rows] = spaced_effect[rows].ljust(42)
    return spaced_effect

def card_print(art, effect, name, c_type, c_id):
    random.seed(int(c_id.replace(" ", "")))
    dmg = str(random.randint(0, 99) * 10)
    random.seed(int(c_id.replace(" ", "")) * 2)
    res = str(random.randint(0, 99) * 10)
    dmg = " " * (3 - len(dmg)) + dmg
    res = res + " " * (3 - len(res))
    final_card = ["┌──────────────────────────────────────────────────┐",
                  "│ ████████████████████████████████████████████████ │",
                  "│ █                                              █ │",
                  "│ █               ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░               █ │",
                  "│ █            ── DIGITAL DUEL CARD ──           █ │",
                  "│ █               ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░               █ │",
                  "│ █                                              █ │",
                  "│ ████████████████████████████████████████████████ │",
                  "├──────────────────────────────────────────────────┤",
                  "│ " + name + " │",
                  "│ " + c_type + " │",
                  "├──────────────────────────────────────────────────┤",
                  "│ █          " + art[0] + "          █ │",
                  "│ █          " + art[1] + "          █ │",
                  "│ █          " + art[2] + "          █ │",
                  "│ █          " + art[3] + "          █ │",
                  "│ █          " + art[4] + "          █ │",
                  "│ █          " + art[5] + "          █ │",
                  "│ █          " + art[6] + "          █ │",
                  "│ █                   [EFFECT]                   █ │",
                  "│ █  " + effect[0] + "  █ │",
                  "│ █  " + effect[1] + "  █ │",
                  "│ █  " + effect[2] + "  █ │",
                  "│ █  " + effect[3] + "  █ │"]
    if c_type.replace(" ", "") == "[PROGRAM]":
        final_card += ["├──────────────────────────────────────────────────┤",
                       "│               DMG / RES: " + dmg + " / " + res + "               │"]
    else:
        final_card += ["│ █  " + effect[4] + "  █ │",
                       "│ █  " + effect[5] + "  █ │"]
    final_card += ["├──────────────────────────────────────────────────┤",
                   "│ █ " + str(c_id) + " █ │",
                   "│ █                                              █ │",
                   "│ ████████████████████████████████████████████████ │",
                   "└──────────────────────────────────────────────────┘"]
    return final_card

print("Welcome to the Digital Duel Card Creator. What are you here for?")
while True:
    start_message = input("→ To create a card (C)\n→ To browse your collection - Card_list.txt (B)\n→ To exit (Q)\n")
    if start_message.upper() == "C":
        while True:
            user_text = ["*********************"] * 5
            while len(user_text[0 and 1 and 2 and 3 and 4]) > 20:
                user_text[0] = input("Enter 5 lines of characters to create a new card"
                                     " (maximum 20 characters per line):\n           Maximum ↓\n")
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

            card_name = input("Enter a name for your card:\n").capitalize()
            card_type = input("Choose a type for your card:\n→ Program (P)\n→ Command (C)\n→ Function (F)\n").lower()
            if card_type == "f":
                card_type = "[FUNCTION]"
            elif card_type == "c":
                card_type = "[COMMAND]"
            else:
                card_type = "[PROGRAM]"
            card_name_full = row_completion_l(card_name)
            card_type_full = row_completion_c(card_type)

            art_list = art_print(user_text, align_choice).split("\n")

            card_effect = "This is an example."
            card_effect = effect_line_return(card_effect)

            print("\n".join(card_print(art_list, card_effect, card_name_full, card_type_full,
                                       row_completion_c("000000", 44))))

            redo = input("Are you satisfied with this rendering? (yes:Y/no:N)\n").upper()
            if redo != "N":
                break

        ascii_sum = 0
        for nbr_lines in range(0, 5):
            ascii_sum += sum(ord(char) for char in user_text[nbr_lines])
        ascii_sum_full = row_completion_c(str(ascii_sum), 44)

        with open("Card_list.txt", "a", encoding="utf-8") as txt_file:
            txt_file.write("│".join(user_text) + "│" + align_choice + "│" + card_name +
                           "│" + card_type + "│" + str(ascii_sum) + "│")

        print("Here is your card:")
        card_effect = effect_line_return(create_effect(ascii_sum, card_type))
        print("\n".join(card_print(art_list, card_effect, card_name_full, card_type_full, ascii_sum_full)))

    elif start_message.upper() == "Q":
        break

    else:
        with open("Card_list.txt", "r", encoding="utf-8") as txt_file:
            card_list = txt_file.read().split("│")

        print("─────────────────────────────────────────────────────────────────────── CARD DATABASE"
              " ──────────────────────────────────────────────────────────────────────\n")
        page_index = 0
        print(row_print(card_list))
        while True:
            user_action = input("→ To search a specific card (S)\n→ To see more result (Enter)\n"
                                "→ To exit this menu (Q)\n").upper()
            if user_action == "S":
                search_criteria = [None, None]
                while True:
                    user_action = input("What type of search do you want to do?\n→ By card name (N)"
                                        "\n→ By card type (T)\n→ By card artwork (A)\n→ By card effect (E)\n").upper()
                    while True:
                        if user_action == "A":
                            search_criteria[0] = input("You are searching for:\n")
                            new_card_list = card_search(card_list, search_criteria[0],
                                                        type_criteria = search_criteria[1])
                            break
                        elif user_action == "T":
                            search_criteria[1] = input("You are searching for:\n→ A [PROGRAM] card (P)"
                                                    "\n→ A [COMMAND] card (C)\n→ A [FUNCTION] card (F)\n").lower()
                            if search_criteria[1] == "f":
                                search_criteria[1] = "[FUNCTION]"
                            elif search_criteria[1] == "c":
                                search_criteria[1] = "[COMMAND]"
                            else:
                                search_criteria[1] = "[PROGRAM]"
                            user_action = input("Do you want to apply another filter on your search?"
                                                " (yes:Y/no:N)\n").upper()
                            if user_action == "N":
                                new_card_list = card_search(card_list, type_criteria = search_criteria[1])
                                break
                            else:
                                user_action = input("What type of search do you want to do?\n→ By card name (N)"
                                                    "\n→ By card artwork (A)\n→ By card effect (E)\n").upper()
                                if user_action == "T":
                                    user_action = "N"
                        elif user_action == "E":
                            search_criteria[0] = input("You are searching for:\n")
                            new_card_list = card_search(card_list, search_criteria[0], 8, 9,
                                                        type_criteria = search_criteria[1])
                            break
                        else:
                            search_criteria[0] = input("You are searching for:\n")
                            new_card_list = card_search(card_list, search_criteria[0], 6, 7,
                                                        type_criteria = search_criteria[1])
                            break
                    print(row_print(new_card_list))
                    user_action = input("→ To search for another card (S)"
                                        "\n→ To see more result (Enter)\n→ To exit this menu (Q)\n").upper()
                    if user_action == "S":
                        pass
                    elif user_action == "":
                        page_index += 1
                        print(row_print(new_card_list, page_index))
                    else:
                        page_index = 0
                        break
            elif user_action == "":
                page_index += 1
                print(row_print(card_list, page_index))
            else:
                break