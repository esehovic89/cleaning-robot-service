import pytest


@pytest.mark.usefixtures("set_test_db")
class TestDBEngine:
    def test_successful_db_engine_get_engine(self) -> None:
        from infrastructure.db.db_engine import DBEngine

        DBEngine.get_engine()

    def test_successful_db_engine_get_engine_singleton(self) -> None:
        from infrastructure.db.db_engine import DBEngine

        engine_one = DBEngine.get_engine()
        engine_two = DBEngine.get_engine()

        assert engine_one == engine_two
