from django.db import models

# Create your models here.


# Each Model represents a table in db
# Each field represents a column in that table

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.last_name},{self.first_name} is {self.age} years old."