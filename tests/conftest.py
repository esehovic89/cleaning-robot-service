import os
from decimal import Decimal
from unittest.mock import patch

import pytest
from starlette.testclient import TestClient

from api.main import app
from src.infrastructure.db.db_engine import Base, DBEngine

client = TestClient(app)


@pytest.fixture
def mock_perf_counter():
    with patch(
        "src.application.cleaning_robot_service.perf_counter",
        side_effect=[Decimal("100.00"), Decimal("100.00123")],
    ) as mock:
        yield mock


@pytest.fixture()
def set_test_db():
    os.environ["DB_ENDPOINT"] = "localhost"
    os.environ["DB_USERNAME"] = "postgres"
    os.environ["DB_PASSWORD"] = "postgres"
    os.environ["DB_NAME"] = "test_db"

    engine = DBEngine.get_engine()

    Base.metadata.create_all(engine)

    yield engine

    Base.metadata.drop_all(engine)
