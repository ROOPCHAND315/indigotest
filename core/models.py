from django.db import models

# Create your models here.
class Book_ticket(models.Model):
    # bookid=models.IntegerField()
    boofrom=models.CharField(max_length=50)
    bookTo=models.CharField(max_length=50)
    dep_date=models.DateField()