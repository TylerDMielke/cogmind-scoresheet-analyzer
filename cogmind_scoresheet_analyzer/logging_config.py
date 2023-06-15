import logging
from typing import Optional

from cogmind_scoresheet_analyzer.config import FILE_ENCODING


def get_logger(
    logger_name: str, log_level: int = logging.INFO, file_log_level: Optional[int] = None
) -> logging.Logger:
    """Get the specified logger.

    Args:
        logger_name: The name of the logger requested.
        log_level: A log level from the logging lib's selection of levels for console.
        file_log_level: A log level from the logging lib's selection of levels for file.

    Returns:
        logging.Logger: The requested logger
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if file_log_level:
        fh = logging.FileHandler(f"{logger_name}.log", encoding=FILE_ENCODING)
        fh.setLevel(file_log_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    logger.info(f"Logging successfully initialized for logger: {logger_name}")

    return logger
