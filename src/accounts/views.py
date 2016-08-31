"""Login view for the users."""

from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

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
        print email, password
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
