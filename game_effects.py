import random

def create_effect(raw_id, c_type):
    with open("Effect_parts.txt", "r", encoding="utf-8") as effect_file:
        effect = effect_file.read().split("\n")
    final_effect = [""] * 5
    for parts in range(0, 5):
        effect_part = [""] * (len(effect) // 5)
        for different_eff in range(0, len(effect) // 5):
            if c_type == "[PROGRAM]":
                effect_part[different_eff] = effect[different_eff * 5 + parts]
            else:
                if "*p*" not in effect[different_eff * 5 + parts]:
                    effect_part[different_eff] = effect[different_eff * 5 + parts]
            effect_part[different_eff] = (effect_part[different_eff].replace("*p*", "")
                                          .replace("*u*", "").replace("*a*", ""))
            if parts != 0 and effect_part[different_eff]:
                effect_part[different_eff] = effect_part[different_eff][0].lower() + effect_part[different_eff][1:]
        if "" in effect_part:
            effect_part.remove("")
        random.seed(int(raw_id) * (parts + 1))
        final_effect[parts] += random.choice(effect_part)
        if parts == 0:
            final_effect[parts] += ","
        elif parts == 3:
            final_effect[parts] += ", then"
    final_effect = " ".join(final_effect) + "."
    return final_effect

print(create_effect(0, "[FUNCTION]"))