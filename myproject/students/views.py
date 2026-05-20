from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from applications.models import Application


@login_required(login_url='student_login')
def student_dashboard(request):

    applications = Application.objects.filter(
        student=request.user
    ).select_related('job')

    return render(
        request,
        'students/student_dashboard.html',
        {
            'applications': applications
        }
    )
