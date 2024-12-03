from api.main import app
from application.cleaning_robot_service import CleaningRobotService
from domain.clean_command import CleanCommand

START_CLEANING_ENDPOINT = "/tibber-developer-test/enter-path/"


@app.post(START_CLEANING_ENDPOINT)
async def clean_endpoint(clean_command_schema: CleanCommand):
    cleaning_robot_service = CleaningRobotService()

    result = cleaning_robot_service.clean(clean_command=clean_command_schema)

    return result.model_dump_json(by_alias=True)
