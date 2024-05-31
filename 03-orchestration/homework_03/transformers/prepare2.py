from typing import Tuple

import pandas as pd

from mlops.utils.data_preparation.encoders import vectorize_features

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(
    df: pd.DataFrame, **kwargs
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    categorical = ['PULocationID', 'DOLocationID']
    X_train, X_val, dv = vectorize_features(df[categorical])
    return X_train, df, dv