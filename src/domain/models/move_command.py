from pydantic import BaseModel

from domain.models.direction_enum import DirectionEnum


class MoveCommand(BaseModel):
    direction: DirectionEnum
    steps: int
