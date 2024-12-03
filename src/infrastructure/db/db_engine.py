from typing import Optional, Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DBEngine:
    _db_engine: Optional[Any] = None

    @staticmethod
    def get_engine() -> Any:
        if DBEngine._db_engine:
            return DBEngine._db_engine

        from infrastructure.db.db_config import (
            DB_NAME,
            DB_ENDPOINT,
            DB_PASSWORD,
            DB_USERNAME,
        )

        DBEngine._db_engine = create_engine(
            url=f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:5432/{DB_NAME}",
            echo=False,
            pool_size=5,
            max_overflow=0,
            pool_recycle=36000,
            pool_pre_ping=True,
            pool_use_lifo=True,
        )

        return DBEngine._db_engine
