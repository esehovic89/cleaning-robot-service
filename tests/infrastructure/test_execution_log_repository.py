from src.infrastructure.execution_log_repository import ExecutionLogRepository
from tests.factory.execution_log_factory import ExecutionLogFactory


class TestExecutionLogRepository:
    def test_save_successful(self, set_test_db):
        test_cleaning_result = ExecutionLogFactory().build()

        repository = ExecutionLogRepository()
        result = repository.save(execution_log=test_cleaning_result)

        assert result == 1
