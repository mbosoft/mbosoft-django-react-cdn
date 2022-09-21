from django.db import models

# Create your models here.


class Book(models.Model):
    title_book = models.CharField(verbose_name='name of book',
        max_length=76, unique=False, blank=False, null=False)
    publishdate_book = models.DateField(unique=False, blank=False, null=False)
    isbn_book = models.CharField(
        max_length=76, unique=False, blank=False, null=False)
