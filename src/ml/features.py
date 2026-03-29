import pandas as pd


def build_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # 1. Enkle avkastninger
    out["return_1"] = out["close"].pct_change(1)

    # 2. Momentum (litt lengre horisont)
    out["momentum_5"] = out["close"].pct_change(5)

    # 3. Volatilitet (standardavvik av returns)
    out["volatility_5"] = out["return_1"].rolling(5).std()

    return out