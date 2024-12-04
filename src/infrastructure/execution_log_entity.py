from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from src.infrastructure.db.db_engine import Base


class ExecutionLogEntity(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow(), nullable=False)
    commands = Column(Integer, nullable=False)
    result = Column(Integer, nullable=False)
    duration = Column(String, nullable=False)
