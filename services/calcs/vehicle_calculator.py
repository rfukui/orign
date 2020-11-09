from ..risks import *
from .risk_calculator import risk_calculator

def vehicle_calculator(input):
    risk = sum(input['risk_questions'])
    risk += risk_by_age(input['age'])
    risk += risk_by_income(input['income'])
    risk += risk_by_vehicle_year(input['vehicle']['year'])

    return risk_calculator(risk)
