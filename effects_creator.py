import pandas as pd
import random as rand

card_effects = pd.read_excel("New_game_effects.xlsx", sheet_name='Feuil1')
card_effects = card_effects.to_dict(orient='list')
del(card_effects["Other Keywords"])

rand.seed(0)
final_effects = ""
for category in card_effects:
    if category == "Triger" or "Action" or "Action Target":
        for element in card_effects[category]:
            if element != "nan":
                del(card_effects[category][card_effects[category].index(element)])
    rand.shuffle(card_effects[category])
    if str(card_effects[category][0]) != "nan":
        final_effects += str(card_effects[category][0]) + " "
print(final_effects)