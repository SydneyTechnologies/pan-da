from django.db import models
from . views import RetrieveLinkView
from django.shortcuts import resolve_url
# Create your models here.
class Links(models.Model):
    # these values will be stored in the database
    # it contains the original link and the other the hash value used for redirecting
    original_link = models.CharField(max_length = 256)
    hash_value = models.CharField(max_length = 10)

    @property
    def download(self):
        return resolve_url("video") + self.hash_value