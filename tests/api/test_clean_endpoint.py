from decimal import Decimal

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api.clean_endpoint import CLEANING_ENDPOINT
from api.main import app
from tests.factory.clean_command_factory import CleanCommandFactory
from tests.factory.cleaning_result_factory import ExecutionLogFactory

client = TestClient(app)


@pytest.mark.usefixtures("set_test_db")
class TestCleanEndpoint:
    def test_clean_endpoint_successful(self, mock_perf_counter) -> None:
        test_clean_command = CleanCommandFactory().build()
        expected_result = ExecutionLogFactory().duration(Decimal("0.00123")).build()

        response = client.post(
            url=CLEANING_ENDPOINT,
            json=test_clean_command.model_dump(),
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == expected_result.model_dump_json()
