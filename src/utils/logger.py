import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_FILE = os.path.join("logs", "ai_soc_engine.log")


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # Console Output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Output
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger