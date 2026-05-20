from django.db import models
from accounts.models import CustomUser

class Job(models.Model):

    JOB_TYPES = (
        ('FULLTIME', 'Full Time'),
        ('INTERNSHIP', 'Internship'),
    )

    recruiter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    skills_required = models.TextField()
    deadline = models.DateField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
