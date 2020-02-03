from django.db import models
from django.urls import reverse  # Used to generate urls by reversing the URL patterns

# Create your models here.
DB_PREFIX = 'viewssandbox'

class CommonField(models.Model):
  created_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(blank=True, null=True)

##### USER INFO FORM #####
# simple user info model
class UserInfo(CommonField):

  STATUS_CHOICES = [
    ('Student', 'Student'),
    ('Professional', 'Professional')
  ]

  first_name = models.CharField(max_length=40, null=False, help_text="Please enter a first name.")
  last_name = models.CharField(max_length=60, null=True)
  attend_date = models.DateField(null=False, blank=False)
  email = models.EmailField(null=False)
  status = models.CharField(max_length=12, choices=STATUS_CHOICES, null=True, blank=True, help_text="Please choose your current position as student or professionsl.")

  def __str__(self):
    return self.first_name

  class Meta:
    ordering = ['first_name']
    #fixes extra s in the admin panel object name
    verbose_name_plural = "User info"

##### PET INFO FORM #####
# simple user info for Modelforms
class DogInfo(CommonField):
  pet_name = models.CharField(max_length=40, null=False, help_text="Please enter a first name.")
  owner_last_name = models.CharField(max_length=60, null=False)
  attend_date = models.DateField(null=False, blank=False)
  email = models.EmailField(null=False)

##### REPORTER / ARTICLE #####
class Reporter(models.Model):
  f_name = models.CharField(max_length=100)
  l_name = models.CharField(max_length=100)

  def __str__(self):
    return '{0}, {1}'.format(self.l_name, self.f_name)

class Article(models.Model):
  reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  pub_date = models.DateField()

  def get_absolute_url(self):
    """
    Returns the url to access a particular author instance.
    """
    return reverse('reporter-detail', args=[str(self.id)])

  def __str__(self):
    return self.title

  class Meta:
    ordering =('title',)