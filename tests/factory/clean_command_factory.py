from domain.models.clean_command import CleanCommand
from domain.models.direction_enum import DirectionEnum
from domain.models.move_command import MoveCommand
from tests.factory.move_command_factory import MoveCommandFactory


class CleanCommandFactory:
    def __init__(self):
        self._start_point = (10, 22)
        self._commands = [
            MoveCommandFactory().build(),
            MoveCommandFactory().direction(DirectionEnum.north).steps(1).build(),
        ]

    def start_point(self, start_point: tuple[int, int]):
        self._start_point = start_point
        return self

    def commands(self, commands: list[MoveCommand]):
        self._commands = commands
        return self

    def build(self) -> CleanCommand:
        return CleanCommand(start_point=self._start_point, commands=self._commands)
