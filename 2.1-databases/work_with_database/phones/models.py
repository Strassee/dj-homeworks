from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # price = models.FloatField()
    price = models.CharField(max_length=10)
    # image = models.ImageField(upload_to='images/')
    image = models.CharField(max_length=100)
    # release_date = models.DateField()
    release_date = models.CharField(max_length=10)
    lte_exists = models.BooleanField()
    slug = models.SlugField()



