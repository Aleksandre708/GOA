def get_european_floor(american_floor):
    if american_floor <= 0:
        return american_floor
    elif 1 <= american_floor < 13:
        return american_floor - 1
    else:  # american_floor >= 13
        return american_floor - 2