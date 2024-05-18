from django.db import models

# Create your models here.
class Employee(models.Model):
  Eid  = models.AutoField(primary_key=True)
  Ename = models.CharField(max_length=200)
  Eemail = models.EmailField()
  Econtact = models.CharField(max_length=15)
  class Meta:
    db_table = 'employee'
  def __str__(self):
    return self.Ename
