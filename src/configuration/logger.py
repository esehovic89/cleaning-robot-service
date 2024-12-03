import logging
import os


class Logger:
    _logger = None

    @staticmethod
    def get_logger() -> logging.Logger:
        if not Logger._logger:
            log_level: str = os.getenv("LOG_LEVEL", "ERROR")
            logging.root.setLevel(log_level)
            Logger._logger = logging.getLogger()
        return Logger._logger
