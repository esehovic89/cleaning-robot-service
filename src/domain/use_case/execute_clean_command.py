from decimal import Decimal
from time import perf_counter

from src.application.cleaning_robot_service import CleaningRobotService
from src.domain.models.clean_command import CleanCommand
from src.domain.models.execution_log import ExecutionLog
from src.infrastructure.execution_log_repository import ExecutionLogRepository


class ExecuteCleanCommand:
    def run(self, clean_command: CleanCommand) -> ExecutionLog:
        cleaning_robot_service = CleaningRobotService()
        executions_repository = ExecutionLogRepository()

        start_time = perf_counter()
        cleaning_steps = cleaning_robot_service.clean(clean_command=clean_command)
        end_time = perf_counter()

        execution_log = ExecutionLog(
            commands=len(clean_command.commands),
            result=cleaning_steps,
            duration=Decimal(str(end_time - start_time)),
        )

        executions_repository.save(execution_log=execution_log)

        print(f"Resultsddfafd: {execution_log.duration}")

        return execution_log
