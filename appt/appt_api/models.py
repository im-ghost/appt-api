from django.db import models

# Create your models here.
class User(models.Model):
  #id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=30)
  """
  age = models.IntergerField()
  appointments = list()
  """
  def __str__(self):
    return self.name
#class Doctor:
#class Patient:
#class Appointment: