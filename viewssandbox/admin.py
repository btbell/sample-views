from django.contrib import admin
from . import models
#from .models import UserInfo, Reporter, Article

# Register your models here.
@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'attend_date')

admin.site.register(models.Reporter)
#admin.site.register(Reporter)

admin.site.register(models.Article)
