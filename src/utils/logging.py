"""Structured logging."""
import logging
from logging.handlers import RotatingFileHandler

def get_logger(name: str, level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = RotatingFileHandler("gefidata.log", maxBytes=10**6, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger