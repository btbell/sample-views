from django.db import models

# Create your models here.
DB_PREFIX = 'viewssandbox'

class CommonField(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

# simple user info model
class UserInfo(CommonField):
    first_name = models.CharField(max_length=40, null=False, help_text="Please enter a first name.")
    last_name = models.CharField(max_length=60, null=True)
    attend_date = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

# simple user info for Modelforms
class DogForm(CommonField):
    pet_name = models.CharField(max_length=40, null=False, help_text="Please enter a first name.")
    owner_last_name = models.CharField(max_length=60, null=False)
    attend_date = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False)