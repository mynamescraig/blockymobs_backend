def physical(types, level, attack_type, opponent_types):
    ## SAFETY CHECKS
    if not isinstance(level, int):
        raise TypeError("level must be an integer")
    if not isinstance(types, list):
        raise TypeError("types must be a list of 2")
    if len(types) != 2:
        raise TypeError("types must be a list of 2")
    if not isinstance(opponent_types, list):
        raise TypeError("opponent types must be a list of 2")
    if len(opponent_types) != 2:
        raise TypeError("opponent types must be a list of 2")

    ## CHECK FOR BUFFS AND DEBUFFS
    ## TODO: Write types and effectiveness table





## INPUTS FOR TESTING PURPOSES
#type1 = input("Type 1: ")
#type2 = input("Type 2: ")

#combined = []
#combined.append(type1)
#combined.append(type2)

#lvl = int(input("Level: "))

#print(physical(combined, lvl))
