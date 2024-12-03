from unittest.mock import patch

import pytest
from fastapi import status

from src.api.cleaning_robot_endpoints import CLEANING_ENDPOINT
from src.api.utils import APPLICATION_UNHANDLED_EXCEPTION_TEXT
from tests.conftest import client
from tests.factory.clean_command_factory import CleanCommandFactory
from tests.factory.cleaning_result_factory import CleaningResultFactory


@pytest.mark.usefixtures("set_test_db")
class TestCleanEndpoint:
    def test_clean_successful(self, mock_perf_counter) -> None:
        test_clean_command = CleanCommandFactory().build()
        expected_result = CleaningResultFactory().build()

        response = client.post(
            url=CLEANING_ENDPOINT,
            json=test_clean_command.model_dump(),
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.text == expected_result.model_dump_json()

    @patch(
        "src.application.cleaning_robot_service.CleaningRobotService.clean",
        side_effect=Exception("Random exception!"),
    )
    def test_clean_return_500(
        self, mock_cleaning_robot_service_clean, mock_perf_counter
    ) -> None:
        test_clean_command = CleanCommandFactory().build()

        response = client.post(
            url=CLEANING_ENDPOINT,
            json=test_clean_command.model_dump(),
        )
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.text == APPLICATION_UNHANDLED_EXCEPTION_TEXT
