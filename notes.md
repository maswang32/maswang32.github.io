## Notes Index
{% for file in site.pages %}
  {% if file.path contains 'notes/' %}
  - [{{ file.title }}]({{ file.url }})
  {% endif %}
{% endfor %}