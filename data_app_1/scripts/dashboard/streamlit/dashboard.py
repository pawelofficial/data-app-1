import plotly.graph_objects as go
import streamlit as st
from snowflake.snowpark.context import get_active_session

session = get_active_session()

tickers = session.sql("select distinct ticker from dev.dev_tables.stocks_indicators").collect()
# cast tickers to a list 
tickers = [ticker[0] for ticker in tickers]

ticker = st.selectbox("Select a ticker", tickers)

df = session.sql(f"select * from dev.dev_tables.stocks_indicators where ticker='{ticker}'").to_pandas()

#st.write(df)

# Create figure with secondary y-axis
fig = go.Figure()

# Add trace for RSI
fig.add_trace(
    go.Scatter(x=df["DATE"], y=df["RSI"], name="RSI", yaxis="y1", line=dict(color="red",dash="dot"))
)

# Add trace for CLOSE
fig.add_trace(
    go.Scatter(x=df["DATE"], y=df["CLOSE"], name="CLOSE", yaxis="y2", line=dict(color="blue"))
)

fig.add_trace(
    go.Scatter(x=df["DATE"], y=df["EMA_10"], name="EMA_10", yaxis="y2", line=dict(color="black"))
)

fig.add_trace(
    go.Scatter(x=df["DATE"], y=df["SMA_10"], name="SMA_10", yaxis="y2", line=dict(color="purple"))
)

# Create axis objects
fig.update_layout(
    title="RSI and Price Action",
    xaxis=dict(title="Date"),
    yaxis=dict(title="RSI", side="left"),
    yaxis2=dict(title="Price", side="right", overlaying="y")
)

# Display the chart in Streamlit
st.plotly_chart(fig)

