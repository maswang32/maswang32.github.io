## Notes Index
{% for file in site.pages %}
  {% if file.path contains 'Notes/' %}
  - [{{ file.title }}]({{ file.url }})
  {% endif %}
{% endfor %}