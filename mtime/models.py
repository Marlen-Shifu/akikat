from django.db import models


class City(models.Model):

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    name = models.CharField(max_length=255)
    shirota = models.CharField(max_length=255)
    dolgota = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)