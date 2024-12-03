from tests.factory.cleaning_result_factory import ExecutionLogFactory
from infrastructure.execution_log_repository import ExecutionLogRepository


class TestExecutionLogRepository:
    def test_save_successful(self, set_test_db):
        test_cleaning_result = ExecutionLogFactory().build()

        repository = ExecutionLogRepository()
        result = repository.save(cleaning_result=test_cleaning_result)

        assert result == 1
