import logging


def get_logger(name: str, level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler() #Send loggene til terminalen (stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)  # setter formatet 
        logger.addHandler(handler)       # legger handler til logger så vi får ut riktig format samt desinasjon til terminal

    logger.setLevel(level.upper())
    return logger
