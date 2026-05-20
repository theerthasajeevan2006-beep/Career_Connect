from django.urls import path
from . import views

urlpatterns = [

    path(
        'recruiter/dashboard/',
        views.recruiter_dashboard,
        name='recruiter_dashboard'
    ),

    path(
        'recruiter/add-job/',
        views.add_job,
        name='add_job'
    ),
    path(
        'recruiter/applicants/',
        views.applicants_list,
        name='applicants_list'
    ),

    path(
        'view-applicants/<int:job_id>/',
        views.view_applicants,
        name='view_applicants'
    ),

    path(
        'update-status/<int:application_id>/<str:status>/',
        views.update_application_status,
        name='update_application_status'
    ),
    path(
    'view-applicants/<int:job_id>/',
    views.view_applicants,
    name='view_applicants'
),

]