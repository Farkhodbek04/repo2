from django.db import models

class Hotels(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 45)
    description = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = 'Hotels'

class Facilities(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 45)
    status = models.CharField(max_length = 25)

    class Meta:
        verbose_name_plural = 'Facilities'

class Customers(models.Model):
    name = models.CharField(max_length = 25)
    opinion = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = 'Customers'

