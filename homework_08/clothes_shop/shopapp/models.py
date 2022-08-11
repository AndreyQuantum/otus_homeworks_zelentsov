from django.db import models
# Create your models here.

class ProductKind(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True)

    @property
    def description_short(self):
        if len(self.description) > 50:
            return self.description[:50] + '...'
        else:
            return self.description

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    kind = models.ForeignKey(ProductKind, on_delete=models.PROTECT, null=True)
    size = models.ManyToManyField('shopapp.Size')
    description = models.TextField(blank=True)

    @property
    def description_short(self):
        if len(self.description) > 50:
            return self.description[:50] + '...'
        else:
            return self.description

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Product #{self.id} {self.name!r}>"

class Size(models.Model):
    name = models.CharField(max_length=3, unique=True)
    eu = models.CharField(max_length=3, unique=True, null=True)
    usa = models.CharField(max_length=3, unique=True,null=True)
    jpn = models.CharField(max_length=3, unique=True,null=True)

    def __str__(self):
        return f'{self.name}, {self.eu}, {self.usa}, {self.jpn}'
