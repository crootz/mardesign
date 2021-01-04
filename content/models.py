from django.db import models


# Create your models here.
class Product(models.Model):
    Size = models.TextChoices('Size', 'S M L')
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=Size.choices)
    colour = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name
