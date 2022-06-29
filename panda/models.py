from django.db import models

# Create your models here.


class Panda(models.Model):
    search = models.CharField(max_length=200, blank=True, null=True)
    download_link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
