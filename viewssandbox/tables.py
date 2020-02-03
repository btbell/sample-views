import django_tables2 as tables
from .models import UserInfo

class UserTable(tables.Table):
  class Meta:
    model = UserInfo
    fields = ('first_name', 'last_name', 'attend_date', 'email', 'status',)