from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime

from infrastructure.db.db_engine import Base


class ExecutionLogEntity(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow(), nullable=False)
    commands = Column(Integer, nullable=False)
    result = Column(Integer, nullable=False)
    duration = Column(String, nullable=False)
