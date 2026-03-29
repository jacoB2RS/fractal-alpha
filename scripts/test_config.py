from src.core.config import load_config
from src.core.logging import get_logger


def main():
    logger = get_logger("test_config")

    logger.info("Starting config test")
    config = load_config()
    logger.info("Config loaded successfully")

    print(config)


if __name__ == "__main__":
    main()