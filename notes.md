## Notes Index
{% for file in site.html_pages %}
  {% if file.path contains 'notes/' %}
  - [{{ file.title }}]({{ file.url }})
  {% endif %}
{% endfor %}