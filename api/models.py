from django.db import models

# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
class Appointment(models.Model):
  
class User(models.Model):
    """Model representing a user(but not a specific copy of a user)."""
    full_name = models.CharField(max_length=20)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    age = models.TextField(max_length=1000, help_text='Enter a brief description of the book') 
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    #genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this user."""
        return reverse('user-detail', args=[str(self.id)])

  