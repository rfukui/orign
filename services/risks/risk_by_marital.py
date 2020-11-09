from config import MARITAL_STATUS_INCREASER, RISK_INCREASE_BY_MARITAL_STATUS

def risk_by_marital(marital_status):

    if marital_status == MARITAL_STATUS_INCREASER:
        return RISK_INCREASE_BY_MARITAL_STATUS
    return 0
