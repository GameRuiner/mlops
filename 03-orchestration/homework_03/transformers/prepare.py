from typing import Tuple

import pandas as pd

from mlops.utils.data_preparation.cleaning import clean

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(
    df: pd.DataFrame, **kwargs
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    df = clean(df)
    return df