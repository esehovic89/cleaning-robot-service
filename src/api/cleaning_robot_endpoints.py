from fastapi import APIRouter

from domain.models.clean_command import CleanCommand
from src.api.cleaning_result import CleaningResult
from src.domain.use_case.execute_clean_command import ExecuteCleanCommand

CLEANING_ENDPOINT = "/tibber-developer-test/enter-path/"

router = APIRouter(tags=["cleaning-robot"])


@router.post(CLEANING_ENDPOINT)
async def clean(clean_command: CleanCommand) -> CleaningResult:
    cleaning_result = ExecuteCleanCommand().run(clean_command=clean_command)

    return CleaningResult(places_cleaned=cleaning_result.result)
