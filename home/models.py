from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122, null=True)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=10)
    text = models.TextField()
    date = models.DateField()
