from sqlalchemy.orm import Session

from domain.execution_log import ExecutionLog
from infrastructure.db.db_engine import DBEngine
from infrastructure.execution_log_entity import ExecutionLogEntity


class ExecutionLogRepository:
    def save(self, cleaning_result: ExecutionLog) -> int:
        engine = DBEngine().get_engine()

        entity = ExecutionLogEntity(**cleaning_result.model_dump())

        with Session(engine) as session:
            session.add(entity)
            session.commit()
            return entity.id
