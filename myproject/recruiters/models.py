from django.db import models
from accounts.models import CustomUser

class RecruiterProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='company_logos/')
    website = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.company_name

# Create your models here.
