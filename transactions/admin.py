# {% extends 'base.html' %}
#
# {% block title %}Kirim/Chiqim qo'shish{% endblock %}
#
# {% block content %}
#     <h1>Kirim/Chiqim qo'shish</h1>
#     <form method="post">
#         {% csrf_token %}
#         {{ form.as_p }}
#         <button type="submit">Submit</button>
#     </form>
# {% endblock %}
