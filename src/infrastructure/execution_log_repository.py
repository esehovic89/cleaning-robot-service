from sqlalchemy.orm import Session

from src.domain.models.execution_log import ExecutionLog
from src.infrastructure.db.db_engine import DBEngine
from src.infrastructure.execution_log_entity import ExecutionLogEntity


class ExecutionLogRepository:
    def save(self, execution_log: ExecutionLog) -> int:
        engine = DBEngine().get_engine()

        entity = ExecutionLogEntity(**execution_log.model_dump())

        with Session(engine) as session:
            session.add(entity)
            session.commit()
            return entity.id
