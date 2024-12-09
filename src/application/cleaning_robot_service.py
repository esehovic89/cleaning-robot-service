from src.domain.models.clean_command import CleanCommand
from src.domain.models.direction_enum import DirectionEnum
from src.domain.models.visited_range import AlignmentEnum, VisitedRange

SINGLE_STEP = 1
X_COORDINATE_KEY = 0
Y_COORDINATE_KEY = 1


class CleaningRobotService:
    def __init__(self):
        self._cleaned_positions = 0
        self._current_position = None
        self._visited_ranges = []

    def clean(self, clean_command: CleanCommand) -> int:
        self._current_position = clean_command.start_point

        for move in clean_command.commands:
            next_point, alignment = self._move(
                move.direction, self._current_position, move.steps
            )

            self._visited_ranges.append(
                VisitedRange(
                    point_one=self._current_position,
                    point_two=next_point,
                    alignment=alignment,
                )
            )

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
        if len(self._visited_ranges) == 0:
            return 1

        number_of_visits = 0
        for visited_range in self._visited_ranges:
            number_of_visits += visited_range.get_distance_between_points()

        return number_of_visits

    def _get_not_unique_visits(self) -> int:
        n = len(self._visited_ranges)
        not_unique = 0
        for i in range(n):
            current_visited_range = self._visited_ranges[i]
            found = set()
            for j in range(i + 1, n):
                next_visited_range = self._visited_ranges[j]
                if (
                    current_visited_range.alignment == AlignmentEnum.horizontal
                    and next_visited_range.alignment == AlignmentEnum.horizontal
                ):
                    d = self._find_horizontal_overlap(
                        current_visited_range, next_visited_range
                    )
                elif (
                    current_visited_range.alignment == AlignmentEnum.vertical
                    and next_visited_range.alignment == AlignmentEnum.vertical
                ):
                    d = self._find_vertical_overlap(
                        current_visited_range, next_visited_range
                    )
                else:
                    d = self._has_intersection(
                        current_visited_range, next_visited_range
                    )

                found.update(d)
            not_unique += len(found)

        return not_unique

    @staticmethod
    def _find_horizontal_overlap(
        segment1: VisitedRange, segment2: VisitedRange
    ) -> set[tuple[int, int]]:
        y1 = segment1.point_one[1]
        y2 = segment2.point_one[1]
        if y1 != y2:
            return set()

        x1_start, x1_end = sorted([segment1.point_one[0], segment1.point_two[0]])
        x2_start, x2_end = sorted([segment2.point_one[0], segment2.point_two[0]])

        overlap_start = max(x1_start, x2_start)
        overlap_end = min(x1_end, x2_end)

        return (
            {(x, y1) for x in range(overlap_start, overlap_end + 1)}
            if overlap_start <= overlap_end
            else set()
        )

    @staticmethod
    def _find_vertical_overlap(
        segment1: VisitedRange, segment2: VisitedRange
    ) -> set[tuple[int, int]]:
        x1 = segment1.point_one[0]
        x2 = segment2.point_one[0]
        if x1 != x2:
            return set()

        y1_start, y1_end = sorted([segment1.point_one[1], segment1.point_two[1]])
        y2_start, y2_end = sorted([segment2.point_one[1], segment2.point_two[1]])

        overlap_start = max(y1_start, y2_start)
        overlap_end = min(y1_end, y2_end)

        return (
            {(x1, y) for y in range(overlap_start, overlap_end + 1)}
            if overlap_start <= overlap_end
            else set()
        )

    @staticmethod
    def _has_intersection(
        range_one: VisitedRange, range_two: VisitedRange
    ) -> set[tuple[int, int]]:
        x1, y1 = range_one.point_one
        x2, y2 = range_one.point_two
        x3, y3 = range_two.point_one
        x4, y4 = range_two.point_two

        if y1 == y2 and x3 == x4:
            if min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4):
                return {(x3, y1)}

        if x1 == x2 and y3 == y4:
            if min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= y3 <= max(y1, y2):
                return {(x1, y3)}

        return set()
