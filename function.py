def sp_card_effects(card_excel_effects):
    an_card_effects = {}
    ro_card_effects = {}
    av_card_effects = {}
    ac_card_effects = {}
    for key in card_excel_effects:
        an_card_effects[key] = []
        ro_card_effects[key] = []
        av_card_effects[key] = []
        ac_card_effects[key] = []
        for j in range(0, len(card_excel_effects[key])):
            card_excel_effects[key][j] = str(card_excel_effects[key][j])
            if "AN*" in card_excel_effects[key][j]:
                an_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
            else:
                if not any(sp in card_excel_effects[key][j] for sp in {"RO*", "AV*", "AC*"}):
                    an_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
            if "RO*" in card_excel_effects[key][j]:
                ro_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
            else:
                if not any(sp in card_excel_effects[key][j] for sp in {"AN*", "AV*", "AC*"}):
                    ro_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
            if "AV*" in card_excel_effects[key][j]:
                av_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
            else:
                if not any(sp in card_excel_effects[key][j] for sp in {"AN*", "RO*", "AC*"}):
                    av_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
            if "AC*" in card_excel_effects[key][j]:
                ac_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
            else:
                if not any(sp in card_excel_effects[key][j] for sp in {"AN*", "RO*", "AV*"}):
                    ac_card_effects[key].append(card_excel_effects[key][j].replace("AN*", "").replace("RO*", "")
                                           .replace("AV*", "").replace("AC*", ""))
    return {"AN":an_card_effects, "RO":ro_card_effects, "AV":av_card_effects, "AC":ac_card_effects}

# print(sp_card_effects({"Test1":["AN*RO*allo", "coco"], "Test2":["bonjour", "amour"]}))
