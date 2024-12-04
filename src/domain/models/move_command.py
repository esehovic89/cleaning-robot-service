from pydantic import BaseModel

from src.domain.models.direction_enum import DirectionEnum


class MoveCommand(BaseModel):
    direction: DirectionEnum
    steps: int
