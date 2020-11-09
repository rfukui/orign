from services.validators import input_validator
from services.calcs import disability_calculator, life_calculator, house_calculator, vehicle_calculator


def insurance_sugestion(input):

    chk_input = input_validator(input)
    if len(chk_input):
        return chk_input

    disability = disability_calculator(input)
    life = life_calculator(input)
    house = house_calculator(input) if 'house' in input else 'ineligible'
    vehicle = vehicle_calculator(input) if 'vehicle' in input else 'ineligible'
    insurances = {'disability': disability,
                  'life': life,
                  'home': house,
                  'auto': vehicle
                  }
    return insurances
