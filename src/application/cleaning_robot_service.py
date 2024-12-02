from decimal import Decimal

from domain.direction_enum import DirectionEnum
from src.domain.clean_command import CleanCommand
from src.domain.cleaning_result import CleaningResult
import time

SINGLE_STEP = 1
X_COORDINATE_KEY = 0
Y_COORDINATE_KEY = 1

class CleaningRobotService:

    def __init__(self):
        self._cleaned_positions = set()
        self._current_position = None


    def clean(self, clean_command: CleanCommand) -> CleaningResult:
        start_time = time.perf_counter()
        self._current_position = clean_command.start

        self._cleaned_positions.add(self._current_position)

        for move in clean_command.commands:
            for _ in range(move.steps):
                self._current_position = self._move(move.direction, self._current_position)
                self._cleaned_positions.add(self._current_position)

        end_time = time.perf_counter()
        return CleaningResult(
            commands=len(clean_command.commands),
            result=len(self._cleaned_positions),
            duration=Decimal(str(end_time-start_time))
        )

    @staticmethod
    def _move(direction, current_position: tuple[int,int]) -> tuple[int,int]:
        next_position = {
            DirectionEnum.east: (current_position[X_COORDINATE_KEY] + SINGLE_STEP, current_position[Y_COORDINATE_KEY]),
            DirectionEnum.west: (current_position[X_COORDINATE_KEY] - SINGLE_STEP, current_position[Y_COORDINATE_KEY]),
            DirectionEnum.north: (current_position[X_COORDINATE_KEY], current_position[Y_COORDINATE_KEY] + SINGLE_STEP),
            DirectionEnum.south: (current_position[X_COORDINATE_KEY], current_position[Y_COORDINATE_KEY] - SINGLE_STEP)
        }
        return next_position.get(direction)
