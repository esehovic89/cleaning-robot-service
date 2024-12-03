from pydantic import BaseModel

from src.domain.move_command import MoveCommand


class CleanCommand(BaseModel):
    start_point: tuple[int, int]
    commands: list[MoveCommand]
