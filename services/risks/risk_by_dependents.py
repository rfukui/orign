from config import MIN_DEPENDENTS_TO_INCREASE_RISK, RISK_INCREASE_BY_DEPENDENTS

def risk_by_dependents(dependents):
    if dependents >= MIN_DEPENDENTS_TO_INCREASE_RISK:
        return RISK_INCREASE_BY_DEPENDENTS
    return 0
