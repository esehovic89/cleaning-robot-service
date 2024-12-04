from src.domain.models.direction_enum import DirectionEnum
from src.domain.models.move_command import MoveCommand


class MoveCommandFactory:
    def __init__(self):
        self._direction = DirectionEnum.east
        self._steps = 2

    def direction(self, direction: DirectionEnum):
        self._direction = direction
        return self

    def steps(self, steps: int):
        self._steps = steps
        return self

    def build(self) -> MoveCommand:
        return MoveCommand(direction=self._direction, steps=self._steps)
