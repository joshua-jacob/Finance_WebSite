from django.db import models
import datetime

# Create your models here.
class pnb(models.Model):

    Date = models.DateField(default=datetime.date.today)
    Description =models.CharField(max_length= 50)
    Withdrawal = models.CharField(max_length= 10)
    Deposit = models.CharField(max_length=10)
    Balance = models.CharField(max_length=10)

class hdfc(models.Model):
    Date = models.DateField(default=datetime.date.today)
    Description =models.CharField(max_length= 50)
    Withdrawal = models.CharField(max_length= 10)
    Deposit = models.CharField(max_length=10)
    Balance = models.CharField(max_length=10)


