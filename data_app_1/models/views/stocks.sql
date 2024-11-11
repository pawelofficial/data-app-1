

-- model union alling all seed files 
-- get seed names 
{% set seed_names = list_seeds() %}
{% do log(" __log seed_names: " ~ seed_names, info=True) %}
-- Generate the UNION ALL query
{% set union_query = [] %}
{% for seed in seed_names %}
    {% do union_query.append("SELECT * FROM " ~var('target_schema')~"." ~ seed) %}
{% endfor %}
{% do log(" __log union_query: " ~ union_query, info=True) %}
{{ union_query | join(" UNION ALL ") }}
