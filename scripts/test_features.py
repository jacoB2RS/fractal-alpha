from src.core.config import load_config
from src.core.logging import get_logger
from src.data.loaders import load_market_data
from src.data.validation import validate_ohlcv_data
from src.ml.features import build_basic_features


def main():
    logger = get_logger("test_features")

    logger.info("Loading config")
    config = load_config()

    logger.info("Loading data")
    df = load_market_data(config["data"]["input_path"])

    logger.info("Validating data")
    validate_ohlcv_data(df)

    logger.info("Building features")
    features = build_basic_features(df)

    logger.info("Features created successfully")

    print(features.tail())


if __name__ == "__main__":
    main()