import pandas as pd

def model(dbt, session):
    dbt.config(
        materialized="table"  # or "view", depending on your needs
    )
    
    df = dbt.ref("stocks").to_pandas()
    columns = list(df.columns)
    
    # Group by ticker and apply transformations
    def calculate_rsi(group):
        group['avg_loss'] = group['CLOSE'].diff().apply(lambda x: x if x < 0 else 0)
        group['avg_gain'] = group['CLOSE'].diff().apply(lambda x: x if x > 0 else 0)
        group['RSI'] = 100 - (100 / (1 + (group['avg_gain'].rolling(window=14).mean() / group['avg_loss'].rolling(window=14).mean().abs())))
        return group
    
    df = df.groupby('TICKER').apply(calculate_rsi)
    columns.append("RSI")
    
    return df[columns]