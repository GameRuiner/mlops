import pandas as pd
from datetime import datetime

options = {
    'key': 'test',
    'secret': 'test',
    'client_kwargs': {
        'endpoint_url': 'http://localhost:4566'
    }
}

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
df_input = pd.DataFrame(data, columns=columns)

bucket_name = 'nyc-duration'
file_name = 'input_file.parquet'
input_file = f's3://{bucket_name}/{file_name}'

df_input.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)