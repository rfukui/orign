from ..risks import *
from .risk_calculator import risk_calculator

from config import MAX_AGE_DISABILTY

def life_calculator(input):
    risk = sum(input['risk_questions'])
    if input['age'] > MAX_AGE_DISABILTY:
        return 'ineligible'
    else:
        risk += risk_by_age(input['age'])
        risk += risk_by_income(input['income'])
        risk += risk_by_dependents(input['dependents'])
        risk += risk_by_marital(input['marital_status'])
        return risk_calculator(risk)
