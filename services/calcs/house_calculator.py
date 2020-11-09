from ..risks import risk_by_age, risk_by_income, risk_by_mortgaged
from .risk_calculator import risk_calculator

def house_calculator(input):
    risk = sum(input['risk_questions'])
    risk += risk_by_age(input['age'])
    risk += risk_by_income(input['income'])
    risk += risk_by_mortgaged(input)

    return risk_calculator(risk)
