:: go to this directory and run this file to load and install dashboard.py to snowflake 

@echo off
snowsql -q "CREATE OR REPLACE STAGE STREAMLIT_STAGE;"


:: Loop through all files in the dashboard directory
for %%f in (dashboard\*) do (
    snowsql -q "PUT file://%%f @STREAMLIT_STAGE AUTO_COMPRESS=FALSE;"
)
snowsql -f .\create_dashboard.sql
