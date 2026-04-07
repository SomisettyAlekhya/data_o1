
def grade_easy(state):
    return min(state["missing_fixed"]/1, 1.0)

def grade_medium(state):
    return min((state["missing_fixed"] + state["duplicates_removed"])/2, 1.0)

def grade_hard(state):
    return min((state["missing_fixed"] + state["duplicates_removed"] + state["type_converted"])/3, 1.0)
