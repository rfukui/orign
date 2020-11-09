from config import MIN_INCOME_TO_RISK_DEDUCTION, RISK_REDUCTION_BY_MIN_INCOME
def risk_by_income(income):
    if income > MIN_INCOME_TO_RISK_DEDUCTION:
        return RISK_REDUCTION_BY_MIN_INCOME
    else:
        return 0
