from django.db import models


class Smartphone(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
