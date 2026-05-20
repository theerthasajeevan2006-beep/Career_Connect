from django.shortcuts import redirect


def student_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated and request.user.role == 'STUDENT':
            return view_func(request, *args, **kwargs)

        return redirect('student_login')

    return wrapper



def recruiter_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated and request.user.role == 'RECRUITER':
            return view_func(request, *args, **kwargs)

        return redirect('recruiter_login')

    return wrapper