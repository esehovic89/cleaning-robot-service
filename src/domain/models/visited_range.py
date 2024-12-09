from enum import Enum
from math import gcd

from pydantic import BaseModel


class AlignmentEnum(str, Enum):
    horizontal = "horizontal"
    vertical = "vertical"


class VisitedRange(BaseModel):
    point_one: tuple[int, int]
    point_two: tuple[int, int]
    alignment: AlignmentEnum

    def get_distance_between_points(self) -> int:
        x1, y1 = self.point_one
        x2, y2 = self.point_two
        return gcd(abs(x2 - x1), abs(y2 - y1)) + 1
