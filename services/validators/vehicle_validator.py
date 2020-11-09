
def vehicle_validator(vehicle):
    if 'year' not in vehicle or type(vehicle['year']) != int or vehicle['year'] < 0:
        return {'ERROR': 'year is required and the expected value is a positive int'}
    return {}
