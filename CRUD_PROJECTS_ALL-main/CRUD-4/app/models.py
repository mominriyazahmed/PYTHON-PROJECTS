from django.db import models

# Create your models here.
class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    details = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Order'