from django.db import models
from django.shortcuts import resolve_url
# Create your models here.
class DownloadLinks(models.Model):
    # these values will be stored in the database
    # it contains the original link and the other the hash value used for redirecting
    original_link = models.CharField(max_length = 256, blank=True, null=True)
    hash_value = models.CharField(max_length = 10, blank=True, null=True)

    @property
    def download(self):
        return resolve_url("video") + self.hash_value