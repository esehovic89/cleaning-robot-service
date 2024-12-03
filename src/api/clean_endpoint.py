from api.main import app
from application.cleaning_robot_service import CleaningRobotService
from domain.clean_command import CleanCommand
from infrastructure.execution_log_repository import ExecutionLogRepository

CLEANING_ENDPOINT = "/tibber-developer-test/enter-path/"


@app.post(CLEANING_ENDPOINT)
async def clean_endpoint(clean_command_schema: CleanCommand):
    cleaning_robot_service = CleaningRobotService()
    executions_repository = ExecutionLogRepository()

    cleaning_result = cleaning_robot_service.clean(clean_command=clean_command_schema)
    executions_repository.save(cleaning_result=cleaning_result)

    return cleaning_result.model_dump_json(by_alias=True)
