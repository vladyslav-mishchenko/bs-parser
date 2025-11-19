from django.db import models
from django.contrib.postgres.fields import ArrayField


class Smartphone(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    dealer = models.CharField(max_length=128, blank=True, null=True)
    product_code = models.CharField(max_length=32, blank=True, null=True)
    price = models.CharField(max_length=16, blank=True, null=True)
    discounted_price = models.CharField(max_length=16, blank=True, null=True)
    reviews = models.CharField(max_length=16, blank=True, null=True)
    image_paths = ArrayField(
        base_field=models.CharField(max_length=255), default=list, blank=True, null=True
    )
    characteristics = models.JSONField(null=True, blank=True)
    internal_memory = models.CharField(max_length=16, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)
    series = models.CharField(max_length=32, blank=True, null=True)
    screen_diagonal = models.CharField(max_length=32, blank=True, null=True)
    display_resolution = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name if self.name is not None else "(no name)"
