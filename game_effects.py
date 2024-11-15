import random

def create_effect(raw_id):
    effect = [""]
    for parts in range(0, 5):
        random.seed(int(raw_id) * (parts + 1))
        effect = random.choices(effect[parts])