from ..risks import risk_by_age, risk_by_income, risk_by_mortgaged, risk_by_dependents, risk_by_marital
from .risk_calculator import risk_calculator
from config import MIN_INCOME_DISABILTY, MAX_AGE_DISABILTY

def disability_calculator(input):
    risk = sum(input['risk_questions'])
    if input['income'] <= MIN_INCOME_DISABILTY or input['age'] > MAX_AGE_DISABILTY:
        return 'ineligible'
    else:
        risk += risk_by_age(input['age'])
        risk += risk_by_income(input['income'])
        risk += risk_by_mortgaged(input)
        risk += risk_by_dependents(input['dependents'])
        risk -= risk_by_marital(input['marital_status'])
        return risk_calculator(risk)
