from django.db import models

class Catalog(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name