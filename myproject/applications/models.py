from django.db import models
from accounts.models import CustomUser
from jobs.models import Job


class Application(models.Model):

    STATUS_CHOICES = (

        ('PENDING', 'Pending'),

        ('SHORTLISTED', 'Shortlisted'),

        ('REJECTED', 'Rejected'),

        ('SELECTED', 'Selected'),
    )

    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    recruiter = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recruiter_applications'
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to='applications/'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    recruiter_message = models.TextField(
        blank=True,
        null=True
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.student.username