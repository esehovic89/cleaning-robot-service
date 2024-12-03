from fastapi import APIRouter

from api.cleaning_result import CleaningResult
from src.application.cleaning_robot_service import CleaningRobotService
from src.domain.clean_command import CleanCommand
from src.infrastructure.execution_log_repository import ExecutionLogRepository

CLEANING_ENDPOINT = "/tibber-developer-test/enter-path/"

router = APIRouter(prefix="/tibber-developer-test", tags=["cleaning-robot"])


@router.post("/enter-path/")
async def clean(clean_command_schema: CleanCommand) -> CleaningResult:
    cleaning_robot_service = CleaningRobotService()
    executions_repository = ExecutionLogRepository()

    cleaning_result = cleaning_robot_service.clean(clean_command=clean_command_schema)
    executions_repository.save(cleaning_result=cleaning_result)

    result = CleaningResult(places_cleaned=cleaning_result.result)

    return result
