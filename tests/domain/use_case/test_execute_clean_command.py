from domain.models.direction_enum import DirectionEnum
from src.domain.use_case.execute_clean_command import ExecuteCleanCommand
from tests.factory.clean_command_factory import CleanCommandFactory
from tests.factory.execution_log_factory import ExecutionLogFactory
from tests.factory.move_command_factory import MoveCommandFactory


class TestExecuteCleanCommand:
    def test_clean_command_one_step_east(
        self, mock_perf_counter, mock_execution_log_repository
    ) -> None:
        test_direction = DirectionEnum.east
        test_steps = 1
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()
        expected_result = ExecutionLogFactory().commands(1).result(2).build()

        service = ExecuteCleanCommand()
        result = service.run(clean_command=test_clean_command)

        assert result == expected_result

        mock_execution_log_repository.assert_called_with(execution_log=expected_result)

    def test_clean_command_zero_commands(
        self, mock_perf_counter, mock_execution_log_repository
    ) -> None:
        test_clean_command = CleanCommandFactory().commands([]).build()
        expected_result = ExecutionLogFactory().commands(0).result(1).build()

        service = ExecuteCleanCommand()
        result = service.run(clean_command=test_clean_command)

        assert result == expected_result

        mock_execution_log_repository.assert_called_with(execution_log=expected_result)
