from django.db import models

# Create your models here.
class Task(models.Model):
    tid = models.AutoField(primary_key=True)
    task = models.CharField(max_length=20)
    time = models.TimeField()
    status = models.BooleanField('Done',default=False)
    def __str__(self):
        return self.task
    class Meta:
        db_table = 'task'