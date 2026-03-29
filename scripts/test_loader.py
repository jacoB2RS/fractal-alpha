from src.core.config import load_config
from src.core.logging import get_logger
from src.data.loaders import load_market_data
from src.data.validation import validate_ohlcv_data


def main():
    logger = get_logger("test_loader")

    logger.info("Loading config")
    config = load_config()

    logger.info("Loading market data")
    df = load_market_data(config["data"]["input_path"])

    logger.info("Validating market data")
    validate_ohlcv_data(df)

    logger.info("Market data validated successfully")
    print(df)


if __name__ == "__main__":
    main()