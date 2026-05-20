from django.db import models
from accounts.models import CustomUser

class StudentProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    education = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Create your models here.
