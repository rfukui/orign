from config import RISK_QUESTIONS_QTD
def risk_validator(risks):
    if type(risks)!=list or len(risks) != RISK_QUESTIONS_QTD:
        return {'ERROR': 'risk_questions must be a array with %s bools' % RISK_QUESTIONS_QTD }
    else:
        for x in risks:
            if x not in [0, 1]:
                return {'ERROR': 'risk_questions must be a array with 3 bool'}
    return {}
