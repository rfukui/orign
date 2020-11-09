def house_validator(house):
    if ('ownership_status' not in house
        or type(house['ownership_status']) != str
        or house['ownership_status'] not in ['owned', 'mortgaged']):
        return {'ERROR': 'ownership_status is required and the expected value is "owned" or "mortgaged"'}
    return {}
