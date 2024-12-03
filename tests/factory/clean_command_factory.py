from domain.clean_command import CleanCommand
from domain.direction_enum import DirectionEnum
from domain.move_command import MoveCommand
from tests.factory.move_command_factory import MoveCommandFactory


class CleanCommandFactory:
    def __init__(self):
        self._start = (10, 22)
        self._commands = [
            MoveCommandFactory().build(),
            MoveCommandFactory().direction(DirectionEnum.north).steps(1).build(),
        ]

    def start(self, start: tuple[int, int]):
        self._start = start
        return self

    def commands(self, commands: list[MoveCommand]):
        self._commands = commands
        return self

    def build(self) -> CleanCommand:
        return CleanCommand(start=self._start, commands=self._commands)
