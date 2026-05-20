from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from jobs.models import Job
from applications.models import Application
from students.models import StudentProfile


# SHOW ALL JOBS
def browse_jobs(request):

    jobs = Job.objects.all()

    return render(
        request,
        'students/browse_jobs.html',
        {'jobs': jobs}
    )


# JOB DETAIL PAGE
def job_detail(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    return render(
        request,
        'students/job_detail.html',
        {'job': job}
    )


# APPLY JOB
@login_required(login_url='student_login')
def apply_job(request, job_id):

    if request.user.role != 'STUDENT':

        messages.error(
            request,
            'Only students can apply.'
        )

        return redirect('home')

    job = get_object_or_404(Job, id=job_id)

    already_applied = Application.objects.filter(
        student=request.user,
        job=job
    ).exists()

    if already_applied:

        messages.warning(
            request,
            'You already applied for this job.'
        )

        return redirect('browse_jobs')

    Application.objects.create(
        student=request.user,
        recruiter=job.recruiter,
        job=job,
        resume=request.user.studentprofile.resume
    )

    messages.success(
        request,
        'Application submitted successfully.'
    )

    return redirect('student_dashboard')
