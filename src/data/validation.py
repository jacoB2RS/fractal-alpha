import pandas as pd


REQUIRED_COLUMNS = ["timestamp", "open", "high", "low", "close", "volume"]


def validate_ohlcv_data(df: pd.DataFrame) -> None:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if df.empty:
        raise ValueError("Input dataframe is empty")

    if df["close"].isna().any():
        raise ValueError("Close column contains missing values")

    if (df["close"] <= 0).any():
        raise ValueError("Close column contains non-positive prices")

    if (df["volume"] < 0).any():
        raise ValueError("Volume column contains negative values")