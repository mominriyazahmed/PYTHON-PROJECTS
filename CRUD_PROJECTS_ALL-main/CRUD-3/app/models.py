from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date_published = models.DateField()
    no_of_pages = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.title