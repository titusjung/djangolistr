from django.views.generic import ListView, TemplateView
from django.contrib.auth import authenticate, login
from listapp.models import Entry

class HomeView(ListView):

    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')

class LoginView(TemplateView):
    template_name = 'login.html'
