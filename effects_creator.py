import pandas as pd
import random as rand

card_effects = pd.read_excel("New_game_effects.xlsx", sheet_name='Feuil1')
card_effects = card_effects.to_dict(orient='list')

rand.seed(5)
nbr_effects = rand.randint(1,3)
for i in range(0,nbr_effects + 1):
    vanilla_effect = rand.randint(0,7)
    final_effects = ""
    if not vanilla_effect:
        for category in card_effects:
            if category != "Other Keywords":
                temp_effects = []
                if category in {"Trigger", "Restriction", "Action", "Action Target"}:
                    for element in card_effects[category]:
                        if str(element) != "nan":
                            temp_effects.append(element)
                    card_effects[category] = temp_effects
                rand.shuffle(card_effects[category])
                if str(card_effects[category][0]) != "nan":
                    if category == "Downside":
                        final_effects += ", but"
                    elif category == "Action":
                        final_effects += " :"
                    elif category == "Spontaneous Trigger":
                        if str(card_effects["Trigger"][0]) == "SPONTANEOUS":
                            final_effects += " " + str(card_effects[category][0])
                    if category not in {"Trigger", "Spontaneous Trigger"}:
                        final_effects += " " + str(card_effects[category][0])
                    elif category == "Trigger":
                        final_effects = str(card_effects[category][0])
        rand.shuffle(card_effects["Other Keywords"])
        if str(card_effects["Other Keywords"][0]) != "nan":
            print(card_effects["Other Keywords"][0])
        final_effects += "."
    if final_effects:
        print(final_effects)