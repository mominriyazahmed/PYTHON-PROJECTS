from django.db import models

# Create your models here.
class Blog(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    date_published = models.DateField()
    class Meta:
        db_table = 'Blog'
    def __str__(self):
        return self.blog