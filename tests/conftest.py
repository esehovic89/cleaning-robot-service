from decimal import Decimal
from unittest.mock import patch

import pytest


@pytest.fixture
def mock_perf_counter():
    with patch(
        "application.cleaning_robot_service.perf_counter",
        side_effect=[Decimal("100.00"), Decimal("100.00123")],
    ) as mock:
        yield mock
