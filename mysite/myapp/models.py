from django.db import models

# Create your models here.

class Expense(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    category=models.CharField(max_length=50)
    date=models.DateField(auto_now=True) #what the parameter does is that it automatically fills the date attribute as of current date and user does not ahve to explicity fill this attribute

    def __str__(self):
        return self.name 