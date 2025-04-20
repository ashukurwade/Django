from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    f_name = models.CharField(max_length=50, verbose_name="First Name")
    l_name = models.CharField(max_length=50, verbose_name="Last Name")
    company_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.f_name} {self.l_name} ({self.employee_id})"