from config import RISK_INCREASE_BY_MORTGAGED

def risk_by_mortgaged(input):
    if 'house' not in input:
        return 0

    if input['house']['ownership_status'] == 'mortgaged':
        return RISK_INCREASE_BY_MORTGAGED
    return 0
