from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Product #{self.id} {self.name!r}>"
# Create your models here.
