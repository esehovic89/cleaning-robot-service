from pydantic import BaseModel

from domain.move_command import MoveCommand


class CleanCommand(BaseModel):
    start: tuple[int, int]
    commands: list[MoveCommand]
