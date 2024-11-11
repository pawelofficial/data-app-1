--https://docs.snowflake.com/en/sql-reference/sql/create-streamlit
CREATE OR REPLACE STREAMLIT hello_streamlit
ROOT_LOCATION = '@DEV.DEV.STREAMLIT_STAGE'
MAIN_FILE = '/dashboard.py'
QUERY_WAREHOUSE = COMPUTE_WH;