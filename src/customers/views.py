"""customers view is in this api."""
# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    """home view template loading."""

    template_name = 'customers/home.html'
