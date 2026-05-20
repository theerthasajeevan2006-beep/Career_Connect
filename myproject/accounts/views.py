from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts.models import CustomUser
from students.models import StudentProfile
from recruiters.models import RecruiterProfile


# HOME PAGE
def home(request):
    return render(request, 'home/home.html')


# STUDENT REGISTER
def student_register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        skills = request.POST['skills']

        resume = request.FILES.get('resume')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='STUDENT'
        )

        StudentProfile.objects.create(
            user=user,
            skills=skills,
            resume=resume
        )

        messages.success(request, 'Student account created successfully')

        return redirect('student_login')

    return render(request, 'accounts/student_register.html')


# RECRUITER REGISTER
def recruiter_register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        company_name = request.POST['company_name']
        description = request.POST['description']

        company_logo = request.FILES.get('company_logo')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='RECRUITER'
        )

        RecruiterProfile.objects.create(
            user=user,
            company_name=company_name,
            description=description,
            company_logo=company_logo
        )

        messages.success(request, 'Recruiter account created successfully')

        return redirect('recruiter_login')

    return render(request, 'accounts/recruiter_register.html')


# STUDENT LOGIN
def student_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.role == 'STUDENT':

            login(request, user)

            return redirect('student_dashboard')

        messages.error(request, 'Invalid student credentials')

    return render(request, 'accounts/login.html')


# RECRUITER LOGIN
def recruiter_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.role == 'RECRUITER':

            login(request, user)

            return redirect('recruiter_dashboard')

        messages.error(request, 'Invalid recruiter credentials')

    return render(request, 'accounts/login.html')


# LOGOUT
def user_logout(request):

    logout(request)

    return redirect('home')

