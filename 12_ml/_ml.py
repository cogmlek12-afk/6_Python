"""
    데이터 로드, 피처 생성 등 기능 모아두는 모듈
"""
import pandas as pd
import numpy as np
from _config import path, prices_path, ENCODING

SEED = 42

def load_merged():
    """ prices, companies, sectors를 결합하여 반환 """
    prices = pd.read_csv(prices_path(),
                         encoding=ENCODING,
                         parse_dates=["date"])
    companies = pd.read_csv(path("companies.csv"), encoding=ENCODING)
    sectors = pd.read_csv(path("sectors.csv"),encoding=ENCODING).rename(columns={"code":"sectorCode","name":"sectorName"})

    df = ( prices
            .merge(companies[["code", "name", "sectorCode", "market"]],
                   how="left", on="code", validate="many_to_one")
            .merge(sectors[["sectorCode", "sectorName"]],
                   how="left", on="sectorCode", validate="many_to_one")
            )

    return df.sort_values(["code", "date"]).reset_index(drop=True)
# ---------------------
# 피처 생성
# ---------------------
FEATURES = [
    "ret_1d",     # 전일 수익률
    "ret_5d",     # 5일 수익률
    "ma5_ratio" ,  # 5일 이동 평균 대비 비율
    "ma20_ratio", # 20일 이동 평균 대비 비율
    "vol20",
    "volume_ratio",
    "range_pct",
]

def add_features(df, shift_features=True):
    """
        피처를 생성하여 반환

        Args
            df : 데이터셋
            shift_features : 모든 피처를 한 칸씩 밀건지 여부

    """

    df = df.sort_values(["code", "date"]).copy()

    g = df.groupby("code")

    df["ret_1d"] = g["close"].transform(lambda s: s.pct_change())
    df["ret_5d"] = g["close"].transform(lambda s: s.pct_change(5))

    df["ma5_ratio"] = df["close"] / g["close"].transform(lambda s: s.rolling(5).mean())
    df["ma20_ratio"] = df["close"] / g["close"].transform(lambda s: s.rolling(20).mean())

    df["vol20"] = g["close"].transform(lambda s: s.pct_change().rolling(20).std())

    df["volume_ratio"] = df["volume"] / g["volume"].transform(lambda s: s.rolling(20).mean())

    df["range_pct"] = ((df["high"] - df["low"]) / df["low"]) * 100

    if shift_features:
        for col in FEATURES:
            df[col] = df.groupby("code")[col].shift(1)

    return df

def add_target(df):

        df = df.sort_values(["code", "date"]).copy()

        df["target_ret"] = df.groupby("code")["close"].pct_change()
        df["target_up"] = (df["target_ret"] > 0).astype("int8")

        return df

def build_dataset(shift_features=True):

    df = load_merged()

    df = add_features(df, shift_features=shift_features)
    df = add_target(df)

    df = df.dropna(subset=FEATURES + ["target_ret", "target_up"]).reset_index(drop=True)

    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=FEATURES).reset_index(drop=True)
    return df


def time_split(df, test_size=0.2):
    """
        시계열 데이터를 학습용, 테스트용으로 분리하여 반환
    """
    cutoff = df["date"].quantile(1 - test_size)

    train = df[df["date"] <= cutoff].reset_index(drop=True)
    test = df[df["date"] > cutoff].reset_index(drop=True)

    return train, test, cutoff

