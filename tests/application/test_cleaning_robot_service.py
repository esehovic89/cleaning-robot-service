import pytest

from src.application.cleaning_robot_service import CleaningRobotService
from src.domain.models.direction_enum import DirectionEnum
from tests.factory.clean_command_factory import CleanCommandFactory
from tests.factory.move_command_factory import MoveCommandFactory


class TestCleaningRobotService:
    def test_robot_clean_zero_commands(self) -> None:
        test_clean_command = CleanCommandFactory().commands([]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 1

    def test_robot_clean_one_step_east(self) -> None:
        test_direction = DirectionEnum.east
        test_steps = 1
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 2

    def test_robot_clean_one_step_west(self) -> None:
        test_direction = DirectionEnum.west
        test_steps = 1
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 2

    def test_robot_clean_one_step_north(self) -> None:
        test_direction = DirectionEnum.north
        test_steps = 1
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 2

    def test_robot_clean_one_step_south(self) -> None:
        test_direction = DirectionEnum.south
        test_steps = 1
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 2

    def test_robot_clean_n_step_east(self) -> None:
        test_direction = DirectionEnum.east
        test_steps = 5
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == test_steps + 1

    def test_robot_clean_n_step_west(self) -> None:
        test_direction = DirectionEnum.west
        test_steps = 5
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == test_steps + 1

    def test_robot_clean_n_step_north(self) -> None:
        test_direction = DirectionEnum.north
        test_steps = 5
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == test_steps + 1

    def test_robot_clean_n_step_south(self) -> None:
        test_direction = DirectionEnum.south
        test_steps = 5
        test_move_command = (
            MoveCommandFactory().direction(test_direction).steps(test_steps).build()
        )
        test_clean_command = CleanCommandFactory().commands([test_move_command]).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == test_steps + 1

    def test_robot_clean_no_repeated_points(self) -> None:
        test_start = (0, 0)

        test_move_east_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.east).steps(1).build()
        )
        test_move_north_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(1).build()
        )
        test_move_west_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.west).steps(1).build()
        )
        test_move_south_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(1).build()
        )
        test_move_patter = [
            test_move_east_one_step_command,
            test_move_north_one_step_command,
            test_move_west_one_step_command,
            test_move_north_one_step_command,
            test_move_east_one_step_command,
            test_move_south_one_step_command,
        ]
        test_clean_command = (
            CleanCommandFactory()
            .start_point(test_start)
            .commands(test_move_patter)
            .build()
        )

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 6

    @pytest.mark.parametrize(
        "test_start_point,expected",
        [((0, 0), 4), ((1, 1), 4), ((-1, 1), 4), ((-1, -1), 4), ((1, -1), 4)],
    )
    def test_robot_clean_in_circle_from_center_and_all_quadrants(
        self, test_start_point, expected
    ) -> None:
        test_move_east_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.east).steps(1).build()
        )
        test_move_north_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(1).build()
        )
        test_move_west_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.west).steps(1).build()
        )
        test_move_south_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(1).build()
        )
        test_move_patter = [
            test_move_east_one_step_command,
            test_move_north_one_step_command,
            test_move_west_one_step_command,
            test_move_south_one_step_command,
        ]

        test_clean_command = (
            CleanCommandFactory()
            .start_point(test_start_point)
            .commands(test_move_patter)
            .build()
        )

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == expected

    def test_robot_clean_in_circle_from_first_quadrant(self) -> None:
        test_start = (1, 1)

        test_move_east_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.east).steps(1).build()
        )
        test_move_north_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(1).build()
        )
        test_move_west_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.west).steps(1).build()
        )
        test_move_south_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(1).build()
        )
        test_move_patter = [
            test_move_east_one_step_command,
            test_move_north_one_step_command,
            test_move_west_one_step_command,
            test_move_south_one_step_command,
        ]

        test_clean_command = (
            CleanCommandFactory()
            .start_point(test_start)
            .commands(test_move_patter)
            .build()
        )

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 4

    def test_robot_clean_in_circle_two_times(self) -> None:
        test_start = (0, 0)

        test_move_east_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.east).steps(1).build()
        )
        test_move_north_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(1).build()
        )
        test_move_west_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.west).steps(1).build()
        )
        test_move_south_one_step_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(1).build()
        )
        test_move_patter = [
            test_move_east_one_step_command,
            test_move_north_one_step_command,
            test_move_west_one_step_command,
            test_move_south_one_step_command,
            test_move_east_one_step_command,
            test_move_north_one_step_command,
            test_move_west_one_step_command,
            test_move_south_one_step_command,
        ]

        test_clean_command = (
            CleanCommandFactory()
            .start_point(test_start)
            .commands(test_move_patter)
            .build()
        )

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 4

    def test_robot_clean_in_circle_map_edge(self) -> None:
        test_start = (-100000, -100000)

        test_move_north_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(100000).build()
        )
        test_move_east_command = (
            MoveCommandFactory().direction(DirectionEnum.east).steps(100000).build()
        )
        test_move_west_command = (
            MoveCommandFactory().direction(DirectionEnum.west).steps(100000).build()
        )
        test_move_south_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(100000).build()
        )
        test_move_patter = [
            test_move_north_command,
            test_move_north_command,
            test_move_east_command,
            test_move_east_command,
            test_move_south_command,
            test_move_south_command,
            test_move_west_command,
            test_move_west_command,
        ]

        test_clean_command = (
            CleanCommandFactory()
            .start_point(test_start)
            .commands(test_move_patter)
            .build()
        )

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 800000

    def test_robot_clean_east_and_west_with_overlap(self) -> None:
        test_move_east_command = (
            MoveCommandFactory().direction(DirectionEnum.east).steps(5).build()
        )
        test_move_west_command = (
            MoveCommandFactory().direction(DirectionEnum.west).steps(2).build()
        )

        test_move_command = [test_move_east_command, test_move_west_command]

        test_clean_command = CleanCommandFactory().commands(test_move_command).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 6

    def test_robot_clean_north_and_south_with_overlap(self) -> None:
        test_move_north_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(5).build()
        )
        test_move_south_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(2).build()
        )

        test_move_command = [test_move_north_command, test_move_south_command]

        test_clean_command = CleanCommandFactory().commands(test_move_command).build()

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 6

    def test_robot_clean_vertical_overlap_circle(self) -> None:
        test_move_north_with_n_steps_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(5).build()
        )
        test_move_south_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(2).build()
        )

        test_move_north_with_less_then_n_steps_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(2).build()
        )

        test_move_command = [
            test_move_north_with_n_steps_command,
            test_move_south_command,
            test_move_north_with_less_then_n_steps_command,
            test_move_south_command,
            test_move_north_with_less_then_n_steps_command,
            test_move_south_command,
        ]

        test_clean_command = (
            CleanCommandFactory()
            .start_point((0, 0))
            .commands(test_move_command)
            .build()
        )

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 6

    def test_robot_clean_in_half_circle_map_edge(self) -> None:
        test_start = (0, 0)

        test_move_north_command = (
            MoveCommandFactory().direction(DirectionEnum.north).steps(2).build()
        )
        test_move_east_command = (
            MoveCommandFactory().direction(DirectionEnum.east).steps(2).build()
        )
        test_move_west_command = (
            MoveCommandFactory().direction(DirectionEnum.west).steps(2).build()
        )
        test_move_south_command = (
            MoveCommandFactory().direction(DirectionEnum.south).steps(2).build()
        )
        test_circle_move_patter = [
            test_move_north_command,
            test_move_north_command,
            test_move_east_command,
            test_move_east_command,
            test_move_west_command,
            test_move_west_command,
            test_move_south_command,
            test_move_south_command,
        ]

        test_clean_command = (
            CleanCommandFactory()
            .start_point(test_start)
            .commands(test_circle_move_patter)
            .build()
        )

        service = CleaningRobotService()
        result = service.clean(clean_command=test_clean_command)

        assert result == 9
