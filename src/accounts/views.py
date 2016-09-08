"""Login view for the users."""

from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from .models import User
# Create your views here.


class LoginView(View):
    """Default Template for the login.

    template loaded here
    """

    def get(self, request):
        """Login view for the users."""
        return render(request, 'login.html')

    def post(self, request):
        """Login view post."""
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': True})


class RegisterView(View):
    """User registration Handled."""

    def get(self, request):
        """Register view."""
        return render(request, 'registration.html')

    def post(self, request):
        """User Registration with credentials."""
        email = request.POST.get('email', None)
        user_name = request.POST.get('username', None)
        password = request.POST.get('password', None)
        User.objects.create_user(email, user_name, password)
        return redirect('login')
