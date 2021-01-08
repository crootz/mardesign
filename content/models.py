from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Product(models.Model):
    Size = models.TextChoices('Size', 'S M L')
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=Size.choices)
    colour = models.CharField(max_length=50)
    image = models.ImageField(default='product_pics/default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name


class ContactInformation(models.Model):
    name = models.CharField(max_length=50)
    neighbourhood = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    street_type = models.CharField(max_length=50)
    house_number = models.IntegerField()
    post_code = models.IntegerField()
    locality = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def clean(self):
        validate_only_one_instance(self)


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("You can only create 1 %s" % model.__name__)
