from decimal import Decimal

from src.domain.execution_log import ExecutionLog


class ExecutionLogFactory:
    def __init__(self):
        self._commands = 2
        self._result = 4
        self._duration = Decimal("0.00123")

    def commands(self, commands: int):
        self._commands = commands
        return self

    def result(self, result: int):
        self._result = result
        return self

    def duration(self, duration: Decimal):
        self._duration = duration
        return self

    def build(self) -> ExecutionLog:
        return ExecutionLog(
            commands=self._commands, result=self._result, duration=self._duration
        )
