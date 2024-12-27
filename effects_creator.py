import pandas as pd
import openpyxl as op
from openpyxl.utils.dataframe import dataframe_to_rows
import random as rand

card_effects = pd.read_excel("New_game_effects.xlsx", sheet_name='Feuil1')
card_effects = card_effects.to_dict(orient='list')
card_type = card_effects.pop("Card Type")
card_keywords = card_effects.pop("Other Keywords")
game_colors = card_effects["Colors"]

card_name = (input("Card Name : ")).upper()
card_id = 0
for char in card_name:
    card_id += ord(char)
rand.seed(card_id)

temp_type = []
for element in card_type:
    if str(element) != "nan":
        temp_type.append(element)
card_type = temp_type
rand.shuffle(card_type)
final_type = card_type[0]
print("Card Type : " + final_type)

temp_colors = []
for element in game_colors:
    if str(element) != "nan":
        temp_colors.append(element)
game_colors = temp_colors
rand.shuffle(game_colors)
final_color = temp_colors[0]
print(final_color)

if final_type not in {"Activator", "Action"}:
    danger_level = rand.randint(0,9)
    print("Danger Level : " + str(danger_level))
else:
    danger_level = None

temp_keywords = []
final_keywords = []
for element in card_keywords:
    if str(element) != "nan":
        temp_keywords.append(element)
rand.shuffle(card_keywords)
for i in range(0, len(temp_keywords)):
    if str(card_keywords[i]) != "nan":
        if final_type in {"Activator", "Action"}:
            if str(card_keywords[i]) != "[DOUBLE AMBUSH]":
                final_keywords.append(card_keywords[i])
        else:
            final_keywords.append(card_keywords[i])
if final_keywords:
    for element in final_keywords:
        print(element + " ")

nbr_effects = rand.randint(1,3)
all_effects = []
all_effects_color = []
all_danger_values = []
all_effects_cost = []
for i in range(0,nbr_effects):
    vanilla_effect = rand.randint(0,5)
    final_effect = ""

    for category in card_effects:
        temp_effects = []
        card_effects["Colors"] = game_colors
        if category in {"Trigger", "Restriction", "Action", "Action Target"}:
            for element in card_effects[category]:
                if str(element) != "nan":
                    temp_effects.append(element)
            card_effects[category] = temp_effects
        if (category == "Colors") and (not vanilla_effect):
            if rand.randint(0,3) == 0:
                rand.shuffle(card_effects[category])
        else:
            rand.shuffle(card_effects[category])
        if category == "Colors":
            if rand.randint(0, 2) != 0:
                card_effects[category][0] = final_color

    if not vanilla_effect:
        for category in card_effects:
            if str(card_effects[category][0]) != "nan":
                if category == "Downside":
                    final_effect += ", but"
                elif category == "Action":
                    final_effect += " :"
                elif category == "Action Target":
                    for j in range(0, str(card_effects[category]).count("specific card tag")):
                        card_effects[category][0] = (
                            (card_effects[category][0]).replace("specific card tag", rand.choice(card_name), 1))
                elif category == "Spontaneous Trigger":
                    if str(card_effects["Trigger"][0]) == "SPONTANEOUS":
                        final_effect += " " + str(card_effects[category][0])
                if category not in {"Trigger", "Spontaneous Trigger", "Colors"}:
                    final_effect += " " + str(card_effects[category][0])
                elif category == "Trigger":
                    final_effect = str(card_effects[category][0])
        final_effect += "."

    if final_type not in {"Activator", "Action"}:
        danger_value = rand.randint(0, 9) * 10 + danger_level * 100
    else:
        danger_value = None

    if final_effect:
        all_effects.append(final_effect)
        print("\n" + final_effect)
    else:
        if final_type not in {"Activator", "Action"}:
            print()
    if danger_value:
        all_danger_values.append(danger_value)
        print("Danger Value : " + str(danger_value))

    effect_cost = rand.randint(0,2)
    if effect_cost == 0:
        card_effects["Colors"][0] = "Gray"
    if card_effects["Colors"][0] in {"Gray", "Black"}:
        effect_cost = None
    if (final_type not in {"Activator", "Action"}) or (not vanilla_effect):
        all_effects_color.append(card_effects["Colors"][0])
        if effect_cost:
            all_effects_cost.append(effect_cost)
            print("Effect Cost : " + str(effect_cost))
        print("Effect Color : " + card_effects["Colors"][0])


card_tag = rand.choice(card_name)
print("\nCard Tag : " + card_tag + "\n\n")

if not final_keywords:
    final_keywords = None

for i in range(0, 3 - len(all_effects)):
    all_effects.append(None)
for i in range(0, 3 - len(all_effects_cost)):
    all_effects_cost.append(None)
for i in range(0, 3 - len(all_effects_color)):
    all_effects_color.append(None)
    all_danger_values.append(None)

card_infos = {"Card Name":card_name, "Card ID":card_id, "Card Type":final_type, "Card Color":final_color,
              "Danger Level":danger_level, "Keywords":final_keywords, "Effect 1":all_effects[0],
              "Effect 1 Cost":all_effects_cost[0], "Effect 1 Color":all_effects_color[0],
              "Effect 1 Danger":all_danger_values[0], "Effect 2":all_effects[1], "Effect 2 Cost":all_effects_cost[1],
              "Effect 2 Color":all_effects_color[1], "Effect 2 Danger":all_danger_values[1], "Effect 3":all_effects[2],
              "Effect 3 Cost":all_effects_cost[2], "Effect 3 Color":all_effects_color[2],
              "Effect 3 Danger":all_danger_values[2], "Tag":card_tag}

df = pd.DataFrame([card_infos])
wb = op.load_workbook("New_game_effects.xlsx")
sheet = wb['Feuil2']
for rows in dataframe_to_rows(df, index=False, header=False):
    sheet.append(rows)
wb.save("New_game_effects.xlsx")
