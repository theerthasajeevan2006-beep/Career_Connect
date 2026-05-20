from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from jobs.models import Job
from applications.models import Application

from accounts.decorators import recruiter_required


# RECRUITER DASHBOARD
@login_required(login_url='recruiter_login')
@recruiter_required
def recruiter_dashboard(request):

    jobs = Job.objects.filter(
        recruiter=request.user
    )

    applications = Application.objects.filter(
        recruiter=request.user
    )

    return render(
        request,
        'recruiters/recruiter_dashboard.html',
        {
            'jobs': jobs,
            'applications': applications
        }
    )
# VIEW ALL APPLICANTS
@login_required(login_url='recruiter_login')
@recruiter_required
def applicants_list(request):

    applications = Application.objects.filter(
        recruiter=request.user
    )

    return render(
        request,
        'recruiters/applicants_list.html',
        {
            'applications': applications
        }
    )


# VIEW APPLICANTS FOR A PARTICULAR JOB
@login_required(login_url='recruiter_login')
@recruiter_required
@login_required(login_url='recruiter_login')
@recruiter_required
def view_applicants(request, job_id):

    # GET JOB
    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    # GET APPLICATIONS
    applications = Application.objects.filter(
        job=job
    ).select_related(
        'student',
        'job'
    )

    return render(
        request,
        'recruiters/view_applicants.html',
        {
            'job': job,
            'applications': applications
        }
    )


# UPDATE APPLICATION STATUS
@login_required(login_url='recruiter_login')
@recruiter_required
def update_application_status(
    request,
    application_id,
    status
):

    application = get_object_or_404(
        Application,
        id=application_id
    )

    # SECURITY CHECK
    if application.recruiter != request.user:

        messages.error(
            request,
            'Unauthorized access'
        )

        return redirect(
            'recruiter_dashboard'
        )

    # UPDATE STATUS
    application.status = status

    # MESSAGE TO STUDENT
    if status == 'SHORTLISTED':

        application.recruiter_message = (
            'Congratulations! '
            'You are shortlisted for the next round.'
        )

    elif status == 'SELECTED':

        application.recruiter_message = (
            'Congratulations! '
            'You are selected for the next phase.'
        )

    elif status == 'REJECTED':

        application.recruiter_message = (
            'Sorry, you are not selected.'
        )

    application.save()

    messages.success(
        request,
        'Application updated successfully.'
    )

    return redirect(
        'view_applicants',
        job_id=application.job.id
    )

# UPDATE APPLICATION STATUS
@login_required(login_url='recruiter_login')
@recruiter_required
def update_application_status(
    request,
    application_id,
    status
):

    application = get_object_or_404(
        Application,
        id=application_id
    )

    # SECURITY CHECK
    if application.recruiter != request.user:

        messages.error(
            request,
            'Unauthorized access'
        )

        return redirect('recruiter_dashboard')

    # UPDATE STATUS
    application.status = status

    # SEND MESSAGE TO STUDENT
    if status == 'SHORTLISTED':

        application.recruiter_message = (
            'Congratulations! '
            'You are shortlisted for the next round.'
        )

    elif status == 'SELECTED':

        application.recruiter_message = (
            'Congratulations! '
            'You are selected for the next phase.'
        )

    elif status == 'REJECTED':

        application.recruiter_message = (
            'Sorry, you are not selected.'
        )

    application.save()

    messages.success(
        request,
        'Application status updated successfully.'
    )

    return redirect(
        'view_applicants',
        job_id=application.job.id
    )


# ADD JOB
@login_required(login_url='recruiter_login')
@recruiter_required
def add_job(request):

    if request.method == 'POST':

        Job.objects.create(

            recruiter=request.user,

            title=request.POST['title'],

            description=request.POST['description'],

            location=request.POST['location'],

            salary=request.POST['salary'],

            skills_required=request.POST['skills_required'],

            deadline=request.POST['deadline'],

            job_type=request.POST['job_type'],
        )

        messages.success(
            request,
            'Job posted successfully.'
        )

        return redirect('recruiter_dashboard')

    return render(
        request,
        'recruiters/add_job.html'
    )