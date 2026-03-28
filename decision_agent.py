def decide(growth, insights):
    if growth > 10:
        return "Strongly Recommended"
    elif growth > 0:
        return "Recommended"
    else:
        return "Not Recommended"