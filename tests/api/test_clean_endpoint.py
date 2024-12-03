from decimal import Decimal
from unittest.mock import patch

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api.clean_endpoint import CLEANING_ENDPOINT
from api.main import APPLICATION_UNHANDLED_EXCEPTION_TEXT, app
from tests.factory.clean_command_factory import CleanCommandFactory
from tests.factory.execution_log_factory import ExecutionLogFactory

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

    @patch(
        "application.cleaning_robot_service.CleaningRobotService.clean",
        side_effect=Exception("Random exception!"),
    )
    def test_clean_endpoint_return_500(
        self, mock_cleaning_robot_service_clean, mock_perf_counter
    ) -> None:
        test_clean_command = CleanCommandFactory().build()

        response = client.post(
            url=CLEANING_ENDPOINT,
            json=test_clean_command.model_dump(),
        )
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.text == APPLICATION_UNHANDLED_EXCEPTION_TEXT
