from decimal import Decimal

from pydantic import BaseModel

class CleaningResult(BaseModel):
    commands: int
    result: int
    duration: Decimal