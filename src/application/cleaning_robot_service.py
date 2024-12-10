from math import gcd

from src.domain.models.alignment_enum import AlignmentEnum
from src.domain.models.clean_command import CleanCommand
from src.domain.models.direction_enum import DirectionEnum

SINGLE_STEP = 1
X_COORDINATE_KEY = 0
Y_COORDINATE_KEY = 1


class CleaningRobotService:
    def __init__(self):
        self._cleaned_positions = 0
        self._current_position = None
        self._visited_ranges = []

    def clean(self, clean_command: CleanCommand) -> int:
        if len(clean_command.commands) == 0:
            return 1

        self._current_position = clean_command.start_point

        for move in clean_command.commands:
            next_point, alignment = self._move(
                move.direction, self._current_position, move.steps
            )
            self._visited_ranges.append((self._current_position, next_point, alignment))

            self._cleaned_positions += move.steps
            self._current_position = next_point

        return self._get_number_of_visits() - self._get_not_unique_visits()

    @staticmethod
    def _move(
        direction, current_position: tuple[int, int], steps: int
    ) -> tuple[tuple[int, int], AlignmentEnum]:
        if direction == DirectionEnum.east:
            return (
                current_position[X_COORDINATE_KEY] + SINGLE_STEP * steps,
                current_position[Y_COORDINATE_KEY],
            ), AlignmentEnum.horizontal
        elif direction == DirectionEnum.west:
            return (
                current_position[X_COORDINATE_KEY] - SINGLE_STEP * steps,
                current_position[Y_COORDINATE_KEY],
            ), AlignmentEnum.horizontal
        elif direction == DirectionEnum.north:
            return (
                current_position[X_COORDINATE_KEY],
                current_position[Y_COORDINATE_KEY] + SINGLE_STEP * steps,
            ), AlignmentEnum.vertical
        elif direction == DirectionEnum.south:
            return (
                current_position[X_COORDINATE_KEY],
                current_position[Y_COORDINATE_KEY] - SINGLE_STEP * steps,
            ), AlignmentEnum.vertical

        raise Exception("Move not implemented")

    def _get_number_of_visits(self) -> int:
        number_of_visits = 0
        for visited_range in self._visited_ranges:
            number_of_visits += self._get_distance_between_points(visited_range)

        return number_of_visits

    def _get_not_unique_visits(self) -> int:
        not_unique = 0
        for i, current_range in enumerate(self._visited_ranges):
            found = set()
            for j, next_range in enumerate(self._visited_ranges[i + 1 :], start=i + 1):
                if current_range[2] == next_range[2] == AlignmentEnum.horizontal:
                    overlap = self._find_horizontal_overlap(current_range, next_range)
                elif current_range[2] == next_range[2] == AlignmentEnum.vertical:
                    overlap = self._find_vertical_overlap(current_range, next_range)
                else:
                    overlap = self._has_intersection(current_range, next_range)

                found.update(overlap)

            not_unique += len(found)

        return not_unique

    @staticmethod
    def _get_distance_between_points(visited_range) -> int:
        x1, y1 = visited_range[0]
        x2, y2 = visited_range[1]
        return gcd(abs(x2 - x1), abs(y2 - y1)) + 1

    @staticmethod
    def _find_horizontal_overlap(
        current_range: tuple[tuple[int, int], tuple[int, int], AlignmentEnum],
        next_range: tuple[tuple[int, int], tuple[int, int], AlignmentEnum],
    ) -> set[tuple[int, int]]:
        y1 = current_range[0][1]
        y2 = next_range[0][1]
        if y1 != y2:
            return set()

        x1_start, x1_end = sorted([current_range[0][0], current_range[1][0]])
        x2_start, x2_end = sorted([next_range[0][0], next_range[1][0]])

        overlap_start = max(x1_start, x2_start)
        overlap_end = min(x1_end, x2_end)

        return (
            {(x, current_range[0][1]) for x in range(overlap_start, overlap_end + 1)}
            if overlap_start <= overlap_end
            else set()
        )

    @staticmethod
    def _find_vertical_overlap(
        current_range: tuple[tuple[int, int], tuple[int, int], AlignmentEnum],
        next_range: tuple[tuple[int, int], tuple[int, int], AlignmentEnum],
    ) -> set[tuple[int, int]]:
        x1 = current_range[0][0]
        x2 = next_range[0][0]
        if x1 != x2:
            return set()

        y1_start, y1_end = sorted([current_range[0][1], current_range[1][1]])
        y2_start, y2_end = sorted([next_range[0][1], next_range[1][1]])

        overlap_start = max(y1_start, y2_start)
        overlap_end = min(y1_end, y2_end)

        return (
            {(current_range[0][0], y) for y in range(overlap_start, overlap_end + 1)}
            if overlap_start <= overlap_end
            else set()
        )

    @staticmethod
    def _has_intersection(
        range_one: tuple[tuple[int, int], tuple[int, int], AlignmentEnum],
        range_two: tuple[tuple[int, int], tuple[int, int], AlignmentEnum],
    ) -> set[tuple[int, int]]:
        x1, y1 = range_one[0]
        x2, y2 = range_one[1]
        x3, y3 = range_two[0]
        x4, y4 = range_two[1]

        if y1 == y2 and x3 == x4:
            if min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4):
                return {(x3, y1)}

        if x1 == x2 and y3 == y4:
            if min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= y3 <= max(y1, y2):
                return {(x1, y3)}

        return set()
