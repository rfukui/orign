from config import RISK_PARAMETERS_POINTS

def risk_calculator(risk):
    if risk <= RISK_PARAMETERS_POINTS['lower']:
        return 'economic'
    if risk > RISK_PARAMETERS_POINTS['lower'] and risk < RISK_PARAMETERS_POINTS['greater']:
        return 'regular'
    else:
        return 'responsible'
