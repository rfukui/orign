from .risk_validator import risk_validator
from .house_validator import house_validator
from .vehicle_validator import vehicle_validator

def input_validator(input):
    positive_int_fields = ['age', 'dependents', 'income']
    if type(input) != dict:
        return {'ERROR': 'you must be post a json'}
    for field in positive_int_fields:
        if field not in input or type(input[field]) != int or input[field] < 0:
            msg = 'the %s is required and must be a positive integer' % field
            return {'ERROR': msg}

    if ('marital_status' not in input
        or input['marital_status'] not in ['single', 'married']):
        return {'ERROR': 'the marital_status is required and the expected value is "single" or "married"'}

    if 'risk_questions' in input:
        chk_risk = risk_validator(input['risk_questions'])
        if len(chk_risk):
            return chk_risk
    else:
        return {'ERROR': 'risk_questions is required'}

    if 'house' in input:
        chk_house = house_validator(input['house'])
        if len(chk_house):
            return chk_house

    if 'vehicle' in input:
        chk_vehicle = vehicle_validator(input['vehicle'])
        if len(chk_vehicle):
            return chk_vehicle

    return {}
