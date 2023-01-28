from apps.earnings.constants import DISABILITY, HEALTH_CARE, PENSION, PIT, SICKNESS


def calc_pension_contr(salary: float, pension: float = PENSION) -> float:
    return salary * (pension / 100)


def calc_disability_contr(salary: float, disability: float = DISABILITY) -> float:
    return salary * (disability / 100)


def calc_sickness_contr(salary: float, sickness: float = SICKNESS) -> float:
    return salary * (sickness / 100)


def calc_health_care_contr(
    salary: float, zus: float, health_care: float = HEALTH_CARE
) -> float:
    return (salary - zus) * (health_care / 100)


def calc_income(salary: float, zus: float) -> float:
    return salary - zus - 250


def calc_income_tax(income: float, pit: int = PIT) -> int:
    return int(income * (pit / 100) - 300)
