from django.db import models

import string
import random

# Create your models here.
class Url(models.Model):
    original_url = models.URLField(unique=True)
    shortened_url = models.CharField(unique=True, blank=True)
    
    # Generate a random short URL if shortened_url field is not already set and then saves the instances
    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) # create random shortened url
        super().save(*args, **kwargs) # save instance
    
    def __str__(self):
        return self.original_url

