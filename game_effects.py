import random

def create_effect(raw_id):
    with open("Effect_parts.txt", "r", encoding="utf-8") as effect_file:
        effect = effect_file.read().split("\n")
    final_effect = [""] * 5
    for parts in range(0, 5):
        effect_part = [""] * (len(effect) // 5)
        for different_eff in range(0, len(effect) // 5):
            effect_part[different_eff] = effect[different_eff * 5 + parts]
            if parts != 0:
                effect_part[different_eff] = effect_part[different_eff][0].lower() + effect_part[different_eff][1:]
        random.seed(int(raw_id) * (parts + 1))
        final_effect[parts] += random.choice(effect_part)
        if parts == 0:
            final_effect[parts] += ","
        elif parts == 3:
            final_effect[parts] += ", then"
    final_effect = " ".join(final_effect) + "."
    return final_effect

print(create_effect(22))