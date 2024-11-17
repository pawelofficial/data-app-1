import pandas as pd
from snowflake.snowpark.functions import col, lag, when,avg
from snowflake.snowpark.window import Window

window_sizes=[10,20,50]



def model(dbt, session):
    dbt.config(
        materialized="table"  # or "view", depending on your needs
    )
    
    df = dbt.ref("stocks").to_spark()
     # Define the window
    window_spec = Window.orderBy("DATE").rowsBetween(-10 + 1, 0)

    # Calculate SMA
    df = df.withColumn("SMA", avg("CLOSE").over(window_spec))
    
    return df