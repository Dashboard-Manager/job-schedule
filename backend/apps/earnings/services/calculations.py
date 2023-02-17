def calc_pension_contr(salary: float, pension: float) -> float:
    return round(salary * (pension / 100), 2)


def calc_disability_contr(salary: float, disability: float) -> float:
    return round(salary * (disability / 100), 2)


def calc_sickness_contr(salary: float, sickness: float) -> float:
    return round(salary * (sickness / 100), 2)


def calc_health_care_contr(salary: float, zus: float, health_care: float) -> float:
    return round((salary - zus) * (health_care / 100), 2)


def calc_income(salary: float, zus: float) -> float:
    result = round(salary - zus - 250, 2)
    return result if result >= 0 else 0


def calc_income_tax(income: float, pit: int) -> int:
    result = int(income * (pit / 100) - 300)
    return result if result >= 0 else 0
