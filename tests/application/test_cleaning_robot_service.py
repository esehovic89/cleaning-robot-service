from decimal import Decimal
from unittest.mock import patch

import pytest

from application.cleaning_robot_service import CleaningRobotService
from src.domain.direction_enum import DirectionEnum
from tests.factory.clean_command_factory import CleanCommandFactory
from tests.factory.cleaning_result_factory import CleaningResultFactory
from tests.factory.move_command_factory import MoveCommandFactory

@pytest.fixture
def mock_perf_counter():
    with patch("application.cleaning_robot_service.time.perf_counter",
               side_effect=[Decimal("100.00"), Decimal("100.00123")]) as mock:
        yield mock

class TestCleaningRobotService:

    def test_robot_clean_one_step_east(self, mock_perf_counter) ->None:
        test_direction = DirectionEnum.east
        test_steps = 1
        test_move_command = MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        expected_result = CleaningResultFactory().commands(1).result(2).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == expected_result

    def test_robot_clean_one_step_west(self,mock_perf_counter) -> None:
        test_direction = DirectionEnum.west
        test_steps = 1
        test_move_command = MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        expected_result = CleaningResultFactory().commands(1).result(2).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == expected_result

    def test_robot_clean_one_step_north(self, mock_perf_counter) -> None:
        test_direction = DirectionEnum.north
        test_steps = 1
        test_move_command = MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        expected_result = CleaningResultFactory().commands(1).result(2).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == expected_result

    def test_robot_clean_one_step_south(self, mock_perf_counter) -> None:
        test_direction = DirectionEnum.south
        test_steps = 1
        test_move_command = MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        expected_result = CleaningResultFactory().commands(1).result(2).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == expected_result

    def test_robot_clean_in_circle(self, mock_perf_counter) -> None:
        test_start = (0,0)

        test_move_east_one_step_command = MoveCommandFactory().direction(DirectionEnum.east).steps(1).build()
        test_move_north_one_step_command = MoveCommandFactory().direction(DirectionEnum.north).steps(1).build()
        test_move_west_one_step_command = MoveCommandFactory().direction(DirectionEnum.west).steps(1).build()
        test_move_south_one_step_command = MoveCommandFactory().direction(DirectionEnum.south).steps(1).build()
        test_circle_move_patter = [test_move_east_one_step_command, test_move_north_one_step_command, test_move_west_one_step_command, test_move_south_one_step_command]

        test_clean_command = CleanCommandFactory().start(test_start).commands(test_circle_move_patter).build()

        expected_result = CleaningResultFactory().commands(4).result(4).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == expected_result



