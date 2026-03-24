from django.db import models

# Create your models here.

class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_desc = models.CharField(max_length=300)
    p_price  = models.IntegerField(default=0)
    p_image = models.ImageField(upload_to="shop/images",default="")
    p_cat = models.CharField(max_length=50,default="")
    p_sub_cat = models.CharField(max_length=50,default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.p_name
