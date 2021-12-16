from django.db import models

# Create your models here.
from django.db import models

GENDER_CHOICES = (
    ('F', "Female"),
    ('M', "Male")
)


# Create your models here.
class Employee_model(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(default='', max_length=20)
    Gender = models.CharField(default='', max_length=2)
    Email = models.EmailField(default='')
    Age = models.DecimalField(decimal_places=2, max_digits=5, default='')
    DOJ = models.TextField(default='')
    Salary = models.IntegerField(default='')

    def __str__(self):
        return self.Name
