from decimal import Decimal
from time import perf_counter

from src.domain.clean_command import CleanCommand
from src.domain.direction_enum import DirectionEnum
from src.domain.execution_log import ExecutionLog

SINGLE_STEP = 1
X_COORDINATE_KEY = 0
Y_COORDINATE_KEY = 1


class CleaningRobotService:
    def __init__(self):
        self._cleaned_positions = set()
        self._current_position = None

    def clean(self, clean_command: CleanCommand) -> ExecutionLog:
        start_time = perf_counter()

        self._current_position = clean_command.start_point
        self._cleaned_positions.add(self._current_position)

        for move in clean_command.commands:
            for _ in range(move.steps):
                self._current_position = self._move(
                    move.direction, self._current_position
                )
                self._cleaned_positions.add(self._current_position)

        end_time = perf_counter()

        return ExecutionLog(
            commands=len(clean_command.commands),
            result=len(self._cleaned_positions),
            duration=Decimal(str(end_time - start_time)),
        )

    @staticmethod
    def _move(direction, current_position: tuple[int, int]) -> tuple[int, int]:
        next_position = {
            DirectionEnum.east: (
                current_position[X_COORDINATE_KEY] + SINGLE_STEP,
                current_position[Y_COORDINATE_KEY],
            ),
            DirectionEnum.west: (
                current_position[X_COORDINATE_KEY] - SINGLE_STEP,
                current_position[Y_COORDINATE_KEY],
            ),
            DirectionEnum.north: (
                current_position[X_COORDINATE_KEY],
                current_position[Y_COORDINATE_KEY] + SINGLE_STEP,
            ),
            DirectionEnum.south: (
                current_position[X_COORDINATE_KEY],
                current_position[Y_COORDINATE_KEY] - SINGLE_STEP,
            ),
        }
        return next_position[direction]
