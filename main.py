import random

random_nbr = random.randint(0,100)

def art_print (text, align = "c"):
    print("*------------*")
    if align == "c":
        for new_lines in range (0, 3):
            if len(text[new_lines]) % 2 == 0:
                print("| " + " " * ((10 - len(text[new_lines])) // 2) + text[new_lines] +
                      " " * ((10 - len(text[new_lines])) // 2) + " |")
            else:
                print("| \u202F\u200A" + " " * ((10 - len(text[new_lines])) // 2) + text[new_lines] +
                      " " * ((10 - len(text[new_lines])) // 2) + "\u202F |")
    elif align == "l":
        for new_lines in range(0, 3):
            print("| " + text[new_lines] + " " * (10 - len(text[new_lines])) + " |")
    elif align == "r":
        for new_lines in range(0, 3):
            print("| " + " " * (10 - len(text[new_lines])) + text[new_lines] + " |")
    print("*------------*")

while True:
    user_text = ["***********","***********","***********"]
    while len(user_text[0 and 1 and 2]) > 10:
        user_text[0] = input("Enter 5 lines of characters to create a new card (maximum 10 characters per line):\n").lower()
        for lines in range (0, 2):
            user_text[lines + 1] = input("").lower()
        if len(user_text[0 and 1 and 2]) > 10:
            print("You have exceeded the character limit in a line.")

    art_print(user_text, "r")

    redo = input("Are you satisfied with this rendering? (yes:Y/no:N)\n")
    if redo.upper() == "Y":
        break

ascii_sum = 0
for nbr_lines in range (0, 3):
    ascii_sum = sum(ord(char) for char in user_text[nbr_lines])
random.seed(ascii_sum)