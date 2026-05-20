from django.urls import path
from . import views

urlpatterns = [

    path('jobs/', views.browse_jobs, name='browse_jobs'),

    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

]