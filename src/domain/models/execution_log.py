from decimal import Decimal

from pydantic import BaseModel


class ExecutionLog(BaseModel):
    commands: int
    result: int
    duration: Decimal
