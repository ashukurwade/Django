from django.db import models

# Create your models here.
from django.core.validators import EmailValidator

class Student(models.Model):
    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('ENG', 'Engineering'),
        ('BUS', 'Business'),
        ('ART', 'Arts'),
        ('SCI', 'Science'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    date_of_birth = models.DateField()
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.course})"