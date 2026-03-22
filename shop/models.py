from django.db import models

# Create your models here.

class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
