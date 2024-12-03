import logging


class TestGetLogger:
    def test_successful_logger_get_logger_with_default_level(self) -> None:
        from configuration.logger import Logger

        logger = Logger.get_logger()

        assert logger.root.level == logging.ERROR

    def test_successful_logger_get_logger_with_set_level(self) -> None:
        import os

        os.environ["LOG_LEVEL"] = "DEBUG"
        from configuration.logger import Logger

        Logger._logger = None

        logger = Logger.get_logger()

        assert logger.root.level == logging.DEBUG

    def test_successful_db_engine_get_logger_singleton(self) -> None:
        from configuration.logger import Logger

        logger_one = Logger.get_logger()
        logger_two = Logger.get_logger()

        assert logger_one == logger_two
