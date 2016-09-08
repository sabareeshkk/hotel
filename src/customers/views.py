"""customers view is in this api."""
# from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    """home view template loading."""

    redirect_field_name = 'login'
    template_name = 'customers/home.html'
