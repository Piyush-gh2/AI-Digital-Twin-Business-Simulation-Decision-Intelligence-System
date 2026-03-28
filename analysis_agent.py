def analyze(current, predicted):
    growth = ((predicted - current) / current) * 100
    return growth