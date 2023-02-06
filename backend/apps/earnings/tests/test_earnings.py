import pytest
from apps.earnings.services import constants


@pytest.fixture
def earnings_data():
    return {
        "constant_pension_contribution": constants.PENSION,
        "constant_disability_contribution": constants.DISABILITY,
        "constant_healt_care_contribution": constants.HEALTH_CARE,
        "constant_sickness_contribution": constants.SICKNESS,
        "constant_PIT": constants.PIT,
    }
