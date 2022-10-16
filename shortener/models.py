from django.db import models

# Create your models here.
class Links(models.Model):
    # these values will be stored in the database
    # it contains the original link and the other the hash value used for redirecting
    original_link = models.CharField(max_length = 256)
    hash_value = models.CharField(max_length = 10)