from datetime import datetime

from config import VEHICLE_AGE_TO_INCREASE_RISK, RISK_INCREASE_BY_VEHICLE_AGE

def risk_by_vehicle_year(year):
    if datetime.now().year - year <= VEHICLE_AGE_TO_INCREASE_RISK:
        return RISK_INCREASE_BY_VEHICLE_AGE
    return 0
