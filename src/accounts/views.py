"""Login view for the users."""

from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views.generic import View

# Create your views here.


class LoginView(View):
    """Default Template for the login.

    template loaded here
    """

    def get(self, request):
        """Login view for the users."""
        return render(request, 'login.html')
