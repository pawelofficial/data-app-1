{% macro list_seeds() %}
    {% set seed_names = [] %}
    {% if execute %}
        {% for node in graph.nodes.values() %}
            {% if node.resource_type == 'seed' %}
                {% do seed_names.append(node.name) %}
            {% endif %}
        {% endfor %}
    {% endif %}
    {{ return(seed_names) }}
{% endmacro %}
