import django_tables2 as tables
from .models import UserInfo

class UserTable(tables.Table):
  class Meta:
    model = UserInfo
    #template_name = "django-tables2/bootstrap.html" - causes can't find error
    fields = ('first_name', 'last_name', 'attend_date', 'email', )