from datetime import datetime
import unittest
import services
ALL_FIELDS_TEST = {
    'age': 35,
    'dependents': 2,
    'house':{ 'ownership_status': 'owned'},
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}
}
HOUSE_MORTGAGED_TEST = {
    'age': 35,
    'dependents': 2,
    'house':{ 'ownership_status': 'mortgaged'},
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}
}
NO_INCOME_TEST = {
    'age': 35,
    'dependents': 2,
    'house': {'ownership_status': 'owned'},
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}
NO_AGE_TEST = {
    'dependents': 2,
    'house': {'ownership_status': 'owned'},
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}
NEGATIVE_AGE_TEST = {
    'dependents': 2,
    'age': -35,
    'house': {'ownership_status': 'owned'},
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}
NO_DEPENDENTS_TEST = {
    'age': 2,
    'house': {'ownership_status': 'owned'},
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}
NEGATIVE_DEPENDENTS_TEST = {
    'age': 2,
    'dependents': -35,
    'house': {'ownership_status': 'owned'},
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}

NO_VEHICLES_TEST = {
    'age': 35,
    'dependents': 2,
    'house': {'ownership_status': 'owned'},
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],

}

NO_HOUSES_TEST = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}
INVALID_HOUSES_TEST = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'house': { 'year': 2018}

}
INVALID_VEHICLES_TEST = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': '2018'}

}
INVALID_RISK_TEST = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'marital_status': 'married',
    'risk_questions': '[0, 1, 0]',
    'vehicle': { 'year': 2018}

}
INVALID_RISK_TEST2 = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'marital_status': 'married',
    'risk_questions': [0, 1, 2],
    'vehicle': { 'year': 2018}

}
NO_RISK_TEST = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'marital_status': 'married',
    'vehicle': { 'year': 2018}

}

INVALID_MARITAL_TEST = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'marital_status': 'marroed',
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}

NO_MARITAL_TEST = {
    'age': 35,
    'dependents': 2,
    'income': 0,
    'risk_questions': [0, 1, 0],
    'vehicle': { 'year': 2018}

}




class TestCheckMethods(unittest.TestCase):

    def test_check_input(self):
        self.assertEqual(services.validators.input_validator(ALL_FIELDS_TEST), {})

    def test_check_input_no_age(self):
        self.assertEqual(services.validators.input_validator(NO_AGE_TEST), {
                         'ERROR': 'the age is required and must be a positive integer'})

    def test_check_input_negative_age(self):
        self.assertEqual(services.validators.input_validator(NEGATIVE_AGE_TEST), {
                         'ERROR': 'the age is required and must be a positive integer'})

    def test_check_input_no_dependents(self):
        self.assertEqual(services.validators.input_validator(NO_DEPENDENTS_TEST), {
                         'ERROR': 'the dependents is required and must be a positive integer'})

    def test_check_input_negative_dependents(self):
        self.assertEqual(services.validators.input_validator(NEGATIVE_DEPENDENTS_TEST), {
                         'ERROR': 'the dependents is required and must be a positive integer'})

    def test_check_input_no_income(self):
        self.assertEqual(services.validators.input_validator(NO_INCOME_TEST), {
                         'ERROR': 'the income is required and must be a positive integer'})

    def test_check_input_negative_dependents(self):
        self.assertEqual(services.validators.input_validator(NEGATIVE_DEPENDENTS_TEST), {
                         'ERROR': 'the dependents is required and must be a positive integer'})

    def test_check_input_no_vehicle(self):
        self.assertEqual(services.validators.input_validator(NO_VEHICLES_TEST), {})

    def test_check_input_no_house(self):
        self.assertEqual(services.validators.input_validator(NO_HOUSES_TEST), {})

    def test_check_input_no_house(self):
        self.assertEqual(services.validators.input_validator(INVALID_HOUSES_TEST), {
                         'ERROR': 'ownership_status is required and the expected value is "owned" or "mortgaged"'})

    def test_check_input_no_marital(self):
        self.assertEqual(services.validators.input_validator(NO_MARITAL_TEST), {
                         'ERROR': 'the marital_status is required and the expected value is "single" or "married"'})

    def test_check_input_invalid_marital(self):
        self.assertEqual(services.validators.input_validator(INVALID_MARITAL_TEST), {
                         'ERROR': 'the marital_status is required and the expected value is "single" or "married"'})

    def test_check_risk_invalid(self):
        self.assertEqual(services.validators.input_validator(INVALID_RISK_TEST), {
                         'ERROR': 'risk_questions must be a array with 3 bools'})

    def test_check_no_risk(self):
        self.assertEqual(services.validators.input_validator(NO_RISK_TEST), {
                         'ERROR': 'risk_questions is required'})

    def test_check_risk_invalid2(self):
        self.assertEqual(services.validators.input_validator(INVALID_RISK_TEST2), {
                         'ERROR': 'risk_questions must be a array with 3 bool'})


class TestRiskMethods(unittest.TestCase):

    def test_risk_age1(self):
        self.assertEqual(services.risks.risk_by_age(29), -2)

    def test_risk_age2(self):
        self.assertEqual(services.risks.risk_by_age(30), -1)

    def test_risk_age3(self):
        self.assertEqual(services.risks.risk_by_age(40), -1)

    def test_risk_age4(self):
        self.assertEqual(services.risks.risk_by_age(41), 0)

    def test_risk_income1(self):
        self.assertEqual(services.risks.risk_by_income(0), 0)

    def test_risk_income2(self):
        self.assertEqual(services.risks.risk_by_income(200000), 0)

    def test_risk_income3(self):
        self.assertEqual(services.risks.risk_by_income(400000), -1)

    def test_risk_by_dependents1(self):
        self.assertEqual(services.risks.risk_by_dependents(0), 0)

    def test_risk_by_dependents2(self):
        self.assertEqual(services.risks.risk_by_dependents(3), 1)

    def test_risk_by_marital1(self):
        self.assertEqual(services.risks.risk_by_marital('married'), 1)

    def test_risk_by_marital2(self):
        self.assertEqual(services.risks.risk_by_marital('single'), 0)

    def test_risk_by_mortgaged1(self):
        self.assertEqual(services.risks.risk_by_mortgaged(HOUSE_MORTGAGED_TEST), 1)

    def test_risk_by_mortgaged2(self):
        ALL_FIELDS_TEST['house']['ownership_status'] = 'owned'
        self.assertEqual(services.risks.risk_by_mortgaged(ALL_FIELDS_TEST), 0)


    def test_risk_by_vehicle_year1(self):
        self.assertEqual(services.risks.risk_by_vehicle_year(datetime.now().year - 6), 0)

    def test_risk_by_vehicle_year3(self):
        self.assertEqual(services.risks.risk_by_vehicle_year(datetime.now().year - 5), 1)


class TestCalcMethods(unittest.TestCase):

    def test_risk_calculator1(self):
        self.assertEqual(services.calcs.risk_calculator(-1), 'economic')

    def test_risk_calculator2(self):
        self.assertEqual(services.calcs.risk_calculator(0), 'economic')

    def test_risk_calculator3(self):
        self.assertEqual(services.calcs.risk_calculator(1), 'regular')

    def test_risk_calculator4(self):
        self.assertEqual(services.calcs.risk_calculator(4), 'responsible')

    def test_disability1(self):
        self.assertEqual(services.calcs.disability_calculator(ALL_FIELDS_TEST), 'ineligible')

    def test_disability2(self):
        ALL_FIELDS_TEST['income'] = 200
        self.assertEqual(services.calcs.disability_calculator(ALL_FIELDS_TEST), 'economic')

    def test_disability3(self):
        ALL_FIELDS_TEST['income'] = 200
        ALL_FIELDS_TEST['age'] = 70
        self.assertEqual(services.calcs.disability_calculator(ALL_FIELDS_TEST), 'ineligible')

    def test_life1(self):
        ALL_FIELDS_TEST['age'] = 50
        self.assertEqual(services.calcs.life_calculator(ALL_FIELDS_TEST), 'responsible')

    def test_life2(self):
        ALL_FIELDS_TEST['age'] = 35
        self.assertEqual(services.calcs.life_calculator(ALL_FIELDS_TEST), 'regular')

    def test_life3(self):
        ALL_FIELDS_TEST['income'] = 300000
        ALL_FIELDS_TEST['age'] = 15
        self.assertEqual(services.calcs.life_calculator(ALL_FIELDS_TEST), 'economic')

    def test_life4(self):
        ALL_FIELDS_TEST['age'] = 70
        self.assertEqual(services.calcs.life_calculator(ALL_FIELDS_TEST), 'ineligible')

    def test_house_calculator1(self):
        ALL_FIELDS_TEST['age'] = 35
        ALL_FIELDS_TEST['income'] = 0
        self.assertEqual(services.calcs.house_calculator(ALL_FIELDS_TEST), 'economic')

    def test_house_calculator2(self):
        ALL_FIELDS_TEST['age'] = 35
        ALL_FIELDS_TEST['income'] = 0
        ALL_FIELDS_TEST['house'] = {'ownership_status': 'mortgaged'}
        self.assertEqual(services.calcs.house_calculator(ALL_FIELDS_TEST), 'regular')

    def test_vehicle_calculator1(self):
        ALL_FIELDS_TEST['age'] = 35
        ALL_FIELDS_TEST['income'] = 0
        ALL_FIELDS_TEST['vehicle']['year'] = datetime.now().year - 1
        self.assertEqual(services.calcs.vehicle_calculator(ALL_FIELDS_TEST),'regular')

    def test_vehicle_calculator2(self):
        ALL_FIELDS_TEST['age'] = 35
        ALL_FIELDS_TEST['income'] = 0
        ALL_FIELDS_TEST['vehicle'] ={'year': 2005}
        self.assertEqual(services.calcs.vehicle_calculator(ALL_FIELDS_TEST), 'economic')


if __name__ == '__main__':
    unittest.main()
