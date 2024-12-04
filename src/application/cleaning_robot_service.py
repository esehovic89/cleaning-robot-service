from src.domain.models.clean_command import CleanCommand
from src.domain.models.direction_enum import DirectionEnum

SINGLE_STEP = 1
X_COORDINATE_KEY = 0
Y_COORDINATE_KEY = 1


class CleaningRobotService:
    def __init__(self):
        self._cleaned_positions = set()
        self._current_position = None

    def clean(self, clean_command: CleanCommand) -> int:
        self._current_position = clean_command.start_point
        self._cleaned_positions.add(self._current_position)

        for move in clean_command.commands:
            for _ in range(move.steps):
                self._current_position = self._move(
                    move.direction, self._current_position
                )

                self._cleaned_positions.add(self._current_position)
        return len(self._cleaned_positions)

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
